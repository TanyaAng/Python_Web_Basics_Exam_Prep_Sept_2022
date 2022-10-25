from django import forms

from GamesPlay.app_profile.models import Profile
from GamesPlay.game.models import Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': '*********'})
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': '*********'})
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()
        return self.instance
