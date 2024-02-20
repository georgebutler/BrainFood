from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["name"]
    
    def __str__(self):
        return self.name

class Store(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="stores/")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-timestamp"]

class Ingredient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="ingredients/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    calories = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-timestamp"]

class Pantry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ingredient = models.ManyToManyField(Ingredient)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-timestamp"]

class PantryItem(models.Model):
    pantry = models.ForeignKey(Pantry, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-timestamp"]
        unique_together = ('pantry', 'ingredient')

class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="meals/")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-timestamp"]

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="recipes/")
    ingredients = models.ManyToManyField(Ingredient)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-timestamp"]

    def get_nutritional_summary(self):
        summary = {'calories': 0, 'proteins': 0, 'carbs': 0, 'fats': 0}
        for ingredient in self.ingredients.all():
            summary['calories'] += ingredient.calories
            # Assume these fields exist and add similar calculations
            # summary['proteins'] += ingredient.proteins
            # summary['carbs'] += ingredient.carbs
            # summary['fats'] += ingredient.fats
        return summary