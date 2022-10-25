from django import forms

from Music_App.album.models import Album
from Music_App.app_profile.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age'}),
        }


class CreateProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hidden_fields()

    def __hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()
        return self.instance
