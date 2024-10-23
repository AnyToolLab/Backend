from django import forms

class QRCodeGIFGenerateForm(forms.Form):
    IMAGE_TYPES = ['image/png', 'image/jpeg', 'image/gif', 'image/webp']

    file = forms.ImageField(
        required=True,
        error_messages={'required': 'Please upload an image.'}
    )
    text = forms.CharField(
        max_length=255,
        required=True,
        error_messages={
            'required': 'This field is required.',
            'max_length': 'Text cannot exceed 255 characters.'
        }
    )

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.content_type not in self.IMAGE_TYPES:
            raise forms.ValidationError('Unsupported file type. Please upload a PNG, JPG, GIF, or WEBP image.')
        return image