from django import forms

from recipes.web_app.models import Recipe


class BaseRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class CreateRecipeForm(BaseRecipeForm):
    pass


class EditRecipeForm(BaseRecipeForm):
    pass


class DeleteRecipeForm(BaseRecipeForm):
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
