from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'Category:{self.name}'

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    time = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/',null=True, blank=True)

    def __str__(self):
        return f'id: {self.id}, {self.title}, {self.category}'

    def full_recipe(self):
        return f'Recipe:{self.title}, Category: {self.category} Description: {self.description} time: {self.time}'

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'