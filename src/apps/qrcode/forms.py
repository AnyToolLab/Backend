from django import forms
import re

class QRCodeGenerateForm(forms.Form):
    SAVE_FORMATS = ['.png', '.jpg', '.svg', '.gif']

    content = forms.CharField(
        max_length=2500,
        required=True,
        error_messages={
            'required': 'Field "content" is required.',
            'max_length': 'content cannot exceed 2500 characters.'
        }
    )

    color = forms.CharField(
        max_length=7,
        required=False,
        error_messages={
            'max_length': 'color must be in hex format (e.g., #FFFFFF).'
        }
    )

    background_img = forms.ImageField(
        required=False,
    )

    save_format = forms.CharField(
        max_length=7,
        required=True,
        error_messages={
            'required': 'Field "save_format" is required.',
            'max_length': 'save_format cannot exceed 7 characters.'
        }
    )

    def clean_color(self):
        color = self.cleaned_data.get('color')
        hex_color_pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'  # Matches #RGB or #RRGGBB

        if not re.match(hex_color_pattern, color):
            raise forms.ValidationError('Invalid color format. Use hex format (e.g., #FFFFFF or #FFF).')

        return color

    def clean_save_format(self):
        save_format = self.cleaned_data.get('save_format')

        if save_format not in self.SAVE_FORMATS:
            raise forms.ValidationError(f'save_format must be in {self.SAVE_FORMATS}')

        return save_format