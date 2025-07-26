from django.shortcuts import render, get_object_or_404
from .models import Category, FoodItem

def food_menu(request):
    foods = FoodItem.objects.all()
    categories = Category.objects.all()
    selected_category = None
    return render(request, 'menu/food_menu.html', {
        'foods': foods,
        'categories': categories,
        'selected_category': selected_category
    })

def food_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    foods = FoodItem.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'menu/food_menu.html', {
        'foods': foods,
        'categories': categories,
        'selected_category': category.name
    })
