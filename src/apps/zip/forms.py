import zipfile

from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    MAX_FILES_SIZE_MB = 1024
    MAX_FILES_SIZE = MAX_FILES_SIZE_MB * 1024 * 1024
    MAX_UPLOADS = 20

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        total_size = 0

        if isinstance(data, (list, tuple)):
            if len(data) > self.MAX_UPLOADS:
                raise forms.ValidationError(
                    f"The maximum number of files to create a zip archive is {self.MAX_UPLOADS}")

            result = []
            for file_data in data:
                file = single_file_clean(file_data, initial)
                total_size += file.size

                if total_size > self.MAX_FILES_SIZE:
                    raise forms.ValidationError(
                        f"The total size of uploaded files exceeds the maximum limit of {self.MAX_FILES_SIZE_MB}MB")

                is_valid = self.validate_file(file)
                if is_valid:
                    result.append(file)
                else:
                    result.append(False)
        else:
            result = single_file_clean(data, initial)
            result = [result] if self.validate_file(result) else [False]

        return result

    def validate_file(self, file):
        if file.size > self.MAX_FILES_SIZE:
            raise forms.ValidationError(
                f"The size of the file exceeds the maximum file size limit of {self.MAX_FILES_SIZE_MB}MB")
        return True


class CreateZipForm(forms.Form):
    files = MultipleFileField()


class ExtractZipForm(forms.Form):
    MAX_FILE_SIZE_MB = 100
    MAX_FILE_SIZE = MAX_FILE_SIZE_MB * 1024 * 1024

    file = forms.FileField(required=True)

    def clean_file(self):
        file = self.cleaned_data.get("file")
        if file.size > self.MAX_FILE_SIZE:
            raise forms.ValidationError(f"File size could not exceed {self.MAX_FILE_SIZE_MB}MB.")

        try:
            with zipfile.ZipFile(file) as zip_file:
                zip_file.testzip()
        except zipfile.BadZipFile:
            raise forms.ValidationError("Uploaded file is not a valid ZIP archive.")
        except RuntimeError as e:
            if 'encrypted' in str(e).lower():
                raise forms.ValidationError("Uploaded ZIP file is password-protected.")
            else:
                raise forms.ValidationError("There was an error processing the ZIP file.")

        return file
