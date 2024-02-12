from django import forms
from .models import Recipe,User


class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email']


# class Recipe(forms.Model):
#     title = forms.CharField(max_length=100)
#     description = forms.CharField(max_length=200)
#     category = forms.IntegerField(default=0)
#     time = forms.IntegerField(default=0)
#     image = forms.ImageField(upload_to='images/',null=True, blank=True)
class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','description','category','time','image']