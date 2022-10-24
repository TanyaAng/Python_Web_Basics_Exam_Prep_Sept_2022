from django import forms

from Music_App.album.models import Album


class DisableFormMixin():
    disable_fields = ()
    fields = None

    def _disable_fields(self):
        if self.disable_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disable_fields
        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                # field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'image': 'Image URL',
        }
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image': forms.TextInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price'}),
        }


class CreateAlbumForm(BaseAlbumForm):
    pass


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(DisableFormMixin, forms.ModelForm):
    disable_fields = ('album_name', 'artist', 'genre', 'description', 'image', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'
