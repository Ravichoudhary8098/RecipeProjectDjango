from django.shortcuts import render, redirect
from vege.models import *


# Create your views here.


def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        Recipe.objects.create(recipe_name=recipe_name,
                              recipe_description=recipe_description,
                              recipe_image=recipe_image, )
        # recipe = Recipe(
        #     recipe_name=recipe_name,
        #     recipe_description=recipe_description,
        #     recipe_image=recipe_image,
        # )
        # Recipe.save(recipe)
        print(data)
        return redirect('/recipes/')

    queryset = Recipe.objects.all()

    if request.GET.get('search_recipe'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search_recipe'))

    context = {'recipes': queryset}
    return render(request, "recipes.html", context)


def delete_recipes(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')


def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes/')

    context = {"recipe": queryset}

    return render(request, "update_recipe.html", context)
