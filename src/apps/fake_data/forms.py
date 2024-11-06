from django import forms

from src.apps.fake_data.utils import FAKE_DATA


class GenerateFakeDataForm(forms.Form):
    FAKE_DATA_CHOICES = FAKE_DATA.keys()
    SAVE_FORMAT_CHOICES = [('csv', 'CSV'), ('json', 'JSON'), ('xml', 'XML')]
    MAX_LEN_FAKE_DATA = 10
    MAX_ROWS = 20

    fake_data = forms.JSONField(required=True)
    # localization = forms.CharField(required=True)
    rows = forms.IntegerField(required=True, min_value=1, max_value=MAX_ROWS)
    save_format = forms.ChoiceField(choices=SAVE_FORMAT_CHOICES, required=True)

    def clean_fake_data(self):
        fake_data = self.cleaned_data['fake_data']
        if not set(fake_data).issubset(self.FAKE_DATA_CHOICES):
            raise forms.ValidationError('Invalid fake data choice')
        if len(fake_data) > self.MAX_LEN_FAKE_DATA:
            raise forms.ValidationError('Too many fake data choices')
        return fake_data






