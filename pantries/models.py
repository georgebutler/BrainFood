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
    image = models.ImageField(upload_to="stores/", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="ingredients/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    calories = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.name

class Pantry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, default="Pantry")
    ingredient = models.ManyToManyField(Ingredient)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Pantry")
        verbose_name_plural = _("Pantries")
        ordering = ["-timestamp"]

    def __str__(self):
        return self.user.username + "'s " + self.name

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

    def __str__(self):
        return self.ingredient.name + " in " + self.pantry.name

class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="meals/", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.name

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="recipes/", null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.name

    def get_nutritional_summary(self):
        summary = {'calories': 0, 'proteins': 0, 'carbs': 0, 'fats': 0}
        for ingredient in self.ingredients.all():
            summary['calories'] += ingredient.calories
            # Assume these fields exist and add similar calculations
            # summary['proteins'] += ingredient.proteins
            # summary['carbs'] += ingredient.carbs
            # summary['fats'] += ingredient.fats
        return summary