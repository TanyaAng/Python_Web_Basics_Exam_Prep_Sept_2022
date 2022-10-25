from django import forms

from notes_app.notes.models import Note


class BaseNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
        labels = {
            'image_url': 'Link to Image',
        }


class CreateNoteForm(BaseNoteForm):
    pass


class EditNoteForm(BaseNoteForm):
    pass


class DeleteNoteForm(BaseNoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__readonly_fields()

    def __readonly_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
