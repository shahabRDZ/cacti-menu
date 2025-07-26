from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_menu, name='food_menu'),
    path('category/<str:category_name>/', views.food_by_category, name='food_by_category'),
]
