""" 
    --creating paths for pages app
 """

from django.urls import path

# importing views of pages app
from . import views  #  .  : it means current directory


# urlpatterns : it is important to use this name
urlpatterns = [
    path('', views.index, name = 'index_1'),
    path('inicio/', views.index, name = 'index_2'),
    path('registro/', views.register_page, name = 'register'),
]



