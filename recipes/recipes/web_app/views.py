from django.shortcuts import render, redirect

from recipes.web_app.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes.web_app.models import Recipe


def get_recipes():
    try:
        return Recipe.objects.all()
    except:
        return None


def home_page(request):
    recipes = get_recipes()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def recipe_create(request):
    if request.method == 'GET':
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def recipe_edit(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'edit.html', context)


def recipe_delete(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'delete.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    recipe_ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': recipe_ingredients,
    }
    return render(request, 'details.html', context)
