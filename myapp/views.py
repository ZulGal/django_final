from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Recipe, User
from .forms import UserAddForm,RecipeAddForm
import random

COUNT = 5
def index (request):
    html = """
    <h1>Привет, меня зовут Алекс</h1>
    <p>Это мой первый сайт на фреймворке Django<br/>Посмотрите на мой сайт.</p>
    """
    return HttpResponse(html)

def recipes_random_view(request):
    recipes = Recipe.objects.all()
    list_recipes = []
    i=0
    while i < COUNT:
        recipe = random.choices(recipes)
        if not recipe in list_recipes:
            list_recipes.append(recipe)
            i+=1
    context={
        'title':'Главная',
        'recipes': list_recipes,
    }
    return render (request,template_name='myapp/recipes_rand.html', context=context)

def recipe_view(request,recipe_id):
   recipe = Recipe.objects.get(id=recipe_id)
   context = {
       'title': 'Рецепт',
       'recipe': recipe.full_recipe(),
   }
   return render(request, template_name='myapp/recipe.html', context=context)


def user_add(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            user = User(name=name, email=email)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserAddForm()
        message = 'Заполните форму'
    return render(request, 'myapp/recipe_form.html', {'form':form, 'message': message})


def recipe_add(request):
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            time = form.cleaned_data['time']
            image = form.cleaned_data['image']
            recipe = Recipe(title=title, description=description, category=category, time=time, image=image)
            recipe.save()
            message = 'Рецепт сохранён'
    else:
        form = RecipeAddForm()
        message = 'Заполните форму'
    return render(request, 'myapp/recipe_form.html', {'form':form, 'message': message})


