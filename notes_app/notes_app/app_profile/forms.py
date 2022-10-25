from django import forms

from notes_app.app_profile.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'image_url')
        labels = {
            'image_url': 'Link to Profile Image',
        }

# class DeleteProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ()
