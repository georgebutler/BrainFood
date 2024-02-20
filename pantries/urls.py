from django.urls import path
from . import views

urlpatterns = [
    # Pantry URLs
    path('', views.PantryListView.as_view(), name='pantry-list'),
    path('<int:pk>/', views.PantryView.as_view(), name='pantry-view'),
    path('create/', views.PantryCreateView.as_view(), name='pantry-create'),
    path('<int:pk>/update/', views.PantryUpdateView.as_view(), name='pantry-update'),
    path('<int:pk>/delete/', views.PantryDeleteView.as_view(), name='pantry-delete'),

    # Category URLs
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    # Store URLs
    path('stores/', views.StoreListView.as_view(), name='store-list'),
    path('store/create/', views.StoreCreateView.as_view(), name='store-create'),
    path('store/<int:pk>/update/', views.StoreUpdateView.as_view(), name='store-update'),
    path('store/<int:pk>/delete/', views.StoreDeleteView.as_view(), name='store-delete'),

    # Ingredient URLs
    path('ingredients/', views.IngredientListView.as_view(), name='ingredient-list'),
    path('ingredient/create/', views.IngredientCreateView.as_view(), name='ingredient-create'),
    path('ingredient/<int:pk>/update/', views.IngredientUpdateView.as_view(), name='ingredient-update'),
    path('ingredient/<int:pk>/delete/', views.IngredientDeleteView.as_view(), name='ingredient-delete'),

    # Meal URLs
    path('meals/', views.MealListView.as_view(), name='meal-list'),
    path('meal/create/', views.MealCreateView.as_view(), name='meal-create'),
    path('meal/<int:pk>/update/', views.MealUpdateView.as_view(), name='meal-update'),
    path('meal/<int:pk>/delete/', views.MealDeleteView.as_view(), name='meal-delete'),

    # Recipe URLs
    path('recipes/', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
]