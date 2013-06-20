from django import forms

class LocationIconForm(forms.Form):
    icon_file = forms.FileField(
        label='Select an icon',
        help_text='File must be a .png'
    )