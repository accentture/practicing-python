from django.contrib import admin

#to check my models in administration panel, I need to import my models
from .models import Article, Category  # . : it indicates that is a file contained in the same directory


# it clas will allows  to display differents fields in adminstration panel
class ArticleAdmin(admin.ModelAdmin) :
    readonly_fields = ('created_at','updated_at') #setting fields that will be only to read

# Register your models here.
# it is important to regiter my models here, when it is registered, it create a CRUD between my administration panel to able to manage all models and information to able to work with database

admin.site.register(Article, ArticleAdmin)    #registering Article
admin.site.register(Category)   #registering 







# ===================== to config name of administration panel
# admin : accesing to admin
title = "Aprendiendo Django - Jonathan Alejandro feo"
admin.site.site_header = title


# ===================== to change second subtitle of website
admin.site.site_title = title

# ===================== to change first subtitle of website
admin.site.index_title = "Mi panel de gestion con Django"
