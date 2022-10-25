from django import forms

from library.app_profile.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'URL'}),
        }


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__readonly_books()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __readonly_books(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
