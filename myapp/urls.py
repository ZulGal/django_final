from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('rand5/', views.recipes_random_view, name = 'recipes_random_view'),
    path('recipe/<int:recipe_id>', views.recipe_view, name='recipe_view'),
    path('recipeadd/',views.recipe_add,name='recipe_add'),
    path('useradd/',views.user_add,name='user_add'),
    # path('orders/<int:user_id>', views.order_view, name='order_view'),
    # path('products/<int:user_id>/<int:days>', views.product_view, name='product_view'),
    # path('products/<int:product_id>/update', views.product_update, name='product_update'),
    # path('products/<int:product_id>/upload', views.product_upload_image, name='product_upload_image'),

]