from django.http import Http404
from django.views import generic
from django.urls import reverse_lazy
from .models import Category, Store, Ingredient, Pantry, Meal, Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

# Pantry Views
class PantryListView(LoginRequiredMixin, generic.ListView):
    model = Pantry
    context_object_name = 'pantries'
    template_name = 'pantries/pantry_list.html'

    def get_object(self, queryset=None):
        """Override to retrieve a pantry based on its index for the current user."""
        if queryset is None:
            queryset = self.get_queryset()
        idx = self.kwargs.get('pk', 0) - 1
        try:
            return queryset[self.request.user][idx]
        except IndexError:
            raise Http404("No pantry found for this index.")

    def get_queryset(self):
        """Return the ordered list of pantries owned by the current user."""
        return list(Pantry.objects.filter(user=self.request.user).order_by('id'))

class PantryView(LoginRequiredMixin, generic.DetailView):
    model = Pantry
    context_object_name = 'pantry'
    template_name = 'pantries/pantry_view.html'

    def get_queryset(self):
        """Override to filter pantries to those owned by the current user."""
        return Pantry.objects.filter(user=self.request.user)

class PantryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Pantry
    fields = ['name', 'ingredient']
    template_name = 'pantries/pantry_form.html'
    success_url = reverse_lazy('pantry-list')

class PantryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Pantry
    fields = ['name', 'ingredient']
    template_name = 'pantries/pantry_form.html'
    success_url = reverse_lazy('pantry-list')

class PantryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Pantry
    template_name = 'pantries/pantry_confirm_delete.html'
    success_url = reverse_lazy('pantry-list')

# Category Views
class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'categories/category_list.html'

class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    fields = ['name']
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Category
    fields = ['name']
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Category
    template_name = 'categories/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')

# Store Views
class StoreListView(generic.ListView):
    model = Store
    context_object_name = 'stores'
    template_name = 'stores/store_list.html'

class StoreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Store
    fields = ['name', 'image']
    template_name = 'stores/store_form.html'
    success_url = reverse_lazy('store-list')

class StoreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Store
    fields = ['name', 'image']
    template_name = 'stores/store_form.html'
    success_url = reverse_lazy('store-list')

class StoreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Store
    template_name = 'stores/store_confirm_delete.html'
    success_url = reverse_lazy('store-list')

# Ingredient Views
class IngredientListView(generic.ListView):
    model = Ingredient
    context_object_name = 'ingredients'
    template_name = 'ingredients/ingredient_list.html'

class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = ['name', 'image', 'category', 'calories']
    template_name = 'ingredients/ingredient_form.html'
    success_url = reverse_lazy('ingredient-list')

class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = ['name', 'image', 'category', 'calories']
    template_name = 'ingredients/ingredient_form.html'
    success_url = reverse_lazy('ingredient-list')

class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    template_name = 'ingredients/ingredient_confirm_delete.html'
    success_url = reverse_lazy('ingredient-list')

# Meal Views
class MealListView(generic.ListView):
    model = Meal
    context_object_name = 'meals'
    template_name = 'meals/meal_list.html'

class MealCreateView(LoginRequiredMixin, generic.CreateView):
    model = Meal
    fields = ['name', 'description', 'image']
    template_name = 'meals/meal_form.html'
    success_url = reverse_lazy('meal-list')

class MealUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Meal
    fields = ['name', 'description', 'image']
    template_name = 'meals/meal_form.html'
    success_url = reverse_lazy('meal-list')

class MealDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Meal
    template_name = 'meals/meal_confirm_delete.html'
    success_url = reverse_lazy('meal-list')

# Recipe Views
class RecipeListView(generic.ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipes/recipe_list.html'

class RecipeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Recipe
    fields = ['name', 'description', 'image', 'ingredients', 'meal']
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-list')

class RecipeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Recipe
    fields = ['name', 'description', 'image', 'ingredients', 'meal']
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-list')

class RecipeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe-list')
