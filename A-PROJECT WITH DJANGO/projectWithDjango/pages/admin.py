from django.contrib import admin

# Register your models here.
from .models import Page

admin.site.register(Page) 


# ================= Configuration of panel
# to create title for administration panel
title = "Proyecto con Django"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle



