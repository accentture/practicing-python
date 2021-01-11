"""learningDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


#importando app con mis vistas
# from miapp import views as views
import miapp.views #reomendable importar cuando tenemos multiples vistas porque es mas concreto

urlpatterns = [
    path('admin/', admin.site.urls),

    #esto sera la página principal
    path('', miapp.views.index, name = 'index'),

    #usando otra ruta para la pagina principal
    path('inicio/', miapp.views.index, name = 'inicio'),

    #creando una url de nuestro proyecto
                     #cargando la funcion  
    path('hola-mundo-django/', miapp.views.hola_mundo, name = 'hola_mundo'),
                                        #dando un nombre a mi funcion

    path('pagina-pruebas/', miapp.views.pagina, name = 'pagina'),
    path('pagina-pruebas/<int:to_redirect>', miapp.views.pagina, name = 'pagina'),
    #to pass params through url
                    #str = type string

    #optional parameters
    path('contacto-dos/', miapp.views.contacto, name = 'contacto'),
    path('contacto-dos/<str:nombre>/', miapp.views.contacto, name = 'contacto'),
    path('contacto-dos/<str:nombre>/<str:apellidos>', miapp.views.contacto, name = 'contacto'),

    #passing params to save in database
    path('crear-articulo/<str:title>/<str:content>/<str:public>', miapp.views.create_article, name = 'create_article'),
    path('articulo/', miapp.views.article, name="article" ),
    path('editar-articulo/<int:id_article>', miapp.views.edit_article), # it is not necessary to set name of path
    path('articulos/', miapp.views.articles, name="articles"),
    path('borrar-articulos/<int:id>', miapp.views.delete_article, name="delete_article"),
    path('save-article-form/', miapp.views.save_article_with_form, name="save_article_with_form"),
    path('create-article-form/', miapp.views.create_article_with_form, name="create_article_with_form"),
]
