
from django.urls import path

from . import views  #  .  : it means current directory

# urlpatterns : it is important to use this name
urlpatterns = [
    path('articulos/', views.list, name = 'list'),
    path('categoria/<int:category_id>', views.category, name = 'category'),
    path('articulo/<int:article_id>', views.article, name = 'article'),
]



