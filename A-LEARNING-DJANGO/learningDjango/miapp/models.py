#this file is created by Django

from django.db import models

# Create your models here.

#every model represent an entidy, for example: category, articles, user, comments, etc
# a model represent a table of database, also a model can represent a specific register of a table 


#after to exiecute migrations, it will create a Table in database
#recomendable to work with name of model in singular, because I will be working with a model doesn't with many
            #creating inheritance to indicate that it is a Model
class Article(models.Model) :

            # defing type of fields in my table
            # to check diferent fields in Django: https://docs.djangoproject.com/en/3.1/ref/models/fields/
    title = models.CharField(max_length=150, verbose_name='Título') #modifiying length in database, after 100, now 150
                                            #passsing verbose_name to settings properties in Spaninsh(administration panel)
    content = models.TextField(verbose_name='Contenido')

    # adding a new field in my database, after it is important apply migrations
    image = models.ImageField(default='null', verbose_name='Imagen')

    public = models.BooleanField(verbose_name='Público')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado') #saving date of saving
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado') #saving date of edition


    # class META of models : it allows to setting a model to intern level between a framework, that is to say : what is the name of model in plural, what is the name of model in singular, what is criteria of order by default
    # to check more search as : meta class django
    class Meta :
        # db_table = ""  # if I change name of my table, I will have to execute migrations again

        verbose_name = 'Articulo' # putting a singular name to a register
        verbose_name_plural = 'Articulos' #name in plural
        ordering = ['created_at'] # ordering by id, 
        

    # magic method of python : it magic method allows to display in a way more understandable my articles in administration panel
    def __str__(self) :

        if self.public :
            public = "(publicado)"
        else : 
            public = "(privado)"
        return f"{self.title} {public}"

class Category(models.Model) :
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta :
        verbose_name = 'Categoria' # putting a singular name to a register
        verbose_name_plural = 'Categorias'

#create a migration is important to able to change a structure in database
# a migration ocurrs when a change ocurrs in database
# one migration must be created by every change
#when I will execute a migration at produccion, migrations are executed automatically and ocurrs changes in database automatically
# when I work in team and I upload my code to a repository, my classmates will execute my migrations, it allows to have the same verion of database between all members of project
# migration is a way to version of database and doesn't only of code


