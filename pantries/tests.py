from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Category, Store, Ingredient, Pantry, PantryItem, Meal, Recipe

class CategoryModelTest(TestCase):
    def test_string_representation(self):
        category = Category.objects.create(name="Fruits")
        self.assertEqual(str(category), category.name)

class StoreModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_store_creation(self):
        store = Store.objects.create(user=self.user, name="Local Store")
        self.assertEqual(store.name, "Local Store")

class IngredientModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.category = Category.objects.create(name="Vegetables")
        self.store = Store.objects.create(user=self.user, name="Farmers Market")

    def test_ingredient_creation(self):
        ingredient = Ingredient.objects.create(
            user=self.user,
            store=self.store,
            name="Carrot",
            category=self.category,
            calories=41
        )
        self.assertEqual(ingredient.name, "Carrot")
        self.assertEqual(ingredient.calories, 41)

class RecipeModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        # Create a Category and Store instance if needed for Ingredient
        self.category = Category.objects.create(name="Vegetables")
        self.store = Store.objects.create(user=self.user, name="Farmers Market")
        
        self.ingredient1 = Ingredient.objects.create(
            user=self.user, name="Ingredient 1", calories=100, category=self.category, store=self.store
        )
        self.ingredient2 = Ingredient.objects.create(
            user=self.user, name="Ingredient 2", calories=200, category=self.category, store=self.store
        )
        
        # Create a Meal instance before creating a Recipe
        self.meal = Meal.objects.create(
            user=self.user, name="Lunch", description="A delicious lunch."
        )
        
        self.recipe = Recipe.objects.create(
            user=self.user, name="New Recipe", meal=self.meal
        )

    def test_add_ingredients_to_recipe(self):
        self.recipe.ingredients.add(self.ingredient1, self.ingredient2)
        self.assertEqual(self.recipe.ingredients.count(), 2)

    def test_get_nutritional_summary(self):
        self.recipe.ingredients.add(self.ingredient1, self.ingredient2)
        summary = self.recipe.get_nutritional_summary()
        self.assertEqual(summary['calories'], 300)  # Adjust according to actual method logic