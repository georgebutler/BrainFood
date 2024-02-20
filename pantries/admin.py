from django.contrib import admin
from .models import Category, Store, Ingredient, Pantry, PantryItem, Meal, Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'timestamp', 'updated')
    list_filter = ('user',)
    search_fields = ('name', 'user__username')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'store', 'calories', 'user', 'timestamp', 'updated')
    list_filter = ('category', 'store', 'user')
    search_fields = ('name', 'category__name', 'store__name', 'user__username')

@admin.register(Pantry)
class PantryAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'updated')
    search_fields = ('user__username',)

@admin.register(PantryItem)
class PantryItemAdmin(admin.ModelAdmin):
    list_display = ('pantry', 'ingredient', 'quantity', 'unit', 'timestamp', 'updated')
    list_filter = ('pantry__user', 'ingredient__category')
    search_fields = ('pantry__user__username', 'ingredient__name')

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'timestamp', 'updated')
    list_filter = ('user',)
    search_fields = ('name', 'user__username')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'meal', 'user', 'timestamp', 'updated')
    list_filter = ('meal', 'user')
    search_fields = ('name', 'meal__name', 'user__username')