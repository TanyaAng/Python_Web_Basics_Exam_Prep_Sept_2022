from django import forms

from GamesPlay.game.models import Game


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class CreateGameForm(BaseGameForm):
    pass


class EditGameForm(BaseGameForm):
    pass


class DeleteGameForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__readonly_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __readonly_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
