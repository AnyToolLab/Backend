from PIL import Image

from django import forms

IMAGES_TYPES = ('png', 'jpg', 'jpeg', 'webp', 'svg')


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.FileField):
    MAX_IMAGE_SIZE = 5 * 1024 * 1024
    MAX_UPLOADS = 10

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            data = data[:self.MAX_UPLOADS]
            result = []
            for file_data in data:
                file = single_file_clean(file_data, initial)
                is_valid = self.validate_image(file)
                if is_valid:
                    result.append(file)
                else:
                    result.append(False)
        else:
            result = single_file_clean(data, initial)
            result = [result] if self.validate_image(result) else [False]
        return result

    def validate_image(self, file):
        if not file.name.lower().endswith(IMAGES_TYPES):
            # raise forms.ValidationError(f'Only images with {IMAGES_TYPES} extensions are allowed.')
            return False

        if file.size > self.MAX_IMAGE_SIZE:
            # raise forms.ValidationError('Image size must be less than 5MB.')
            return False

        try:
            image = Image.open(file)
            image.verify()
        except Exception as e:
            # raise forms.ValidationError(f'{file.name} is not a valid image.')
            return False
        return True


class ImageConverterForm(forms.Form):
    images = MultipleImageField()
    convert_to_formats = forms.JSONField()

    def clean_convert_to_formats(self):
        convert_to_formats = self.cleaned_data.get('convert_to_formats')
        return [i if i.lower() in IMAGES_TYPES else False for i in convert_to_formats]
