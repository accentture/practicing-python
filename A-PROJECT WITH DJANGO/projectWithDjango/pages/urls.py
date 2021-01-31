""" 
    --creating paths for pages app
 """

from django.urls import path
from . import views # importing views of pages app


# urlpatterns : it is important to use this name
urlpatterns = [
    path('pagina/', views.page, name = 'page'),
    path('pagina/<str:slug>', views.page, name = 'page'), 
]



