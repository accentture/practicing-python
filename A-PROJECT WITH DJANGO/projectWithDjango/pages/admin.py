from django.contrib import admin

# Register your models here.
from .models import Page

#extra configurations
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', )

    #to add a searcher
                #setting name of fields that use to sechear in searcher
    search_fields = ('title', 'content')

    #to add a menu that allows to manage display only field visible
    list_filter = ('visible', ) # comma to end, it allows to interpret that it is a tuple

    # to display columns of description of all Pages
    list_display = ('title', 'visible', 'created_at')

    #to order
    ordering = ('created_at',)      # to invert order : ('-created_at',)

 
admin.site.register(Page, PageAdmin) 

# ================= Configuration of panel
# to create title for administration panel
title = "Proyecto con Django"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle



