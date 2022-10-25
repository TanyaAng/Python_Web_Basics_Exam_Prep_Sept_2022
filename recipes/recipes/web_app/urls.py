from django.urls import path

from recipes.web_app.views import home_page, recipe_create, recipe_edit, recipe_delete, recipe_details

urlpatterns = (
    path('', home_page, name='home page'),
    path('create/', recipe_create, name='recipe create'),
    path('edit/<int:pk>', recipe_edit, name='recipe edit'),
    path('delete/<int:pk>', recipe_delete, name='recipe delete'),
    path('details/<int:pk>', recipe_details, name='recipe details'),
)
