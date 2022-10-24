from django import forms

from Music_App.app_profile.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age'}),
        }


# class DeleteProfileForm(forms.ModelForm):
#     def save(self, commit=True):
#         if commit:
#             self.instance.delete()
#         return self.instance
