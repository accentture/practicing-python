from django.db import models

from ckeditor.fields import RichTextField

#importing user model
from django.contrib.auth.models import User

#It is important to mention that django has user model by default

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length = 100, verbose_name = 'Nombre')
    description = models.CharField(max_length = 255, verbose_name = 'Descripcion')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "Creado el")

    class Meta :
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self) :
        return self.name # when I will print an object of this type, then will print self.name

class Article(models.Model) :

    #the arguments of every field can be orgaized in any order

    title = models.CharField(max_length = 150, verbose_name = 'Titulo')
    content = RichTextField(verbose_name = 'contenido')

                                                                            # upload_to = 'articles'  : indicating where will be saved image
    image = models.ImageField(default = 'null', verbose_name = 'Imagen', upload_to = 'articles') # null because it is not necessary that it field has an image
    public = models.BooleanField(verbose_name = '¿Publicado?')

    #to relationate with user model
                                                        # on_delete = models.CASCADE : it allows to eliminate for example all articles if I remove an user

                                                        #PROTECT instead of CASCADE : in case that I don't want remove register of aricles

                                                        # null = True if I want this field empty
                                # editable= False : it evits that user that create a article is editable or changeable
    user = models.ForeignKey(User, editable = False, verbose_name = 'Usuario', on_delete = models.CASCADE) # when I get user field, it will return a complete object of User, it means that there will nested object between Article object

    #a relation of one to many
                                                              # null = True : because nothing happens if this field haven´t nathing
    categories = models.ManyToManyField(Category, verbose_name = 'Categorias', null = True, blank = True, related_name = "the_inverse_relation")  # ManyToManyField : it means many articles can have many categories
        # related_name : related_name allows any thing
    #other exmaples : ManyToOneField

    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "Creado el")
    updated_at = models.DateTimeField(auto_now = True, verbose_name = "Editado el")

    class Meta :
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

        # indicating criteria of order
        ordering = ['-created_at'] # symbol -  : it allows to order in reverse way

    def __str__(self) :
        return self.title 


