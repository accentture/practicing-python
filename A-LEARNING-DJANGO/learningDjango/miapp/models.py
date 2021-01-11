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
    title = models.CharField(max_length=150) #modifiying length in database, after 100, now 150
    content = models.TextField()

    # adding a new field in my database, after it is important apply migrations
    image = models.ImageField(default='null')

    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True) #saving date of saving
    updated_at = models.DateTimeField(auto_now=True) #saving date of edition

class Category(models.Model) :
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

#create a migration is important to able to change a structure in database
# a migration ocurrs when a change ocurrs in database
# one migration must be created by every change
#when I will execute a migration at produccion, migrations are executed automatically and ocurrs changes in database automatically
# when I work in team and I upload my code to a repository, my classmates will execute my migrations, it allows to have the same verion of database between all members of project
# migration is a way to version of database and doesn't only of code