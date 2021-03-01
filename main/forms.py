from django import forms

# other forms: https://docs.djangoproject.com/en/3.1/topics/forms/#field-data
class CreateNewList(forms.Form):
    name = forms.CharField(label="Name")
    check = forms.BooleanField(required=False)