from django.contrib import admin
from .models import Category, Article

# creation of this class allows to display date
class CategoryAdmin(admin.ModelAdmin) :
    readonly_fields = ('created_at', ) # , : this comma allows to interpret as a tuple

    #to add columns
    list_display = ('name', 'created_at')

    #to add searcher
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin) :
    readonly_fields = ('user', 'created_at', 'updated_at')

                                        # user__username, categories__name  of the table relation
    search_fields = ('title', 'content', 'user__username', 'categories__name')

    #to add columns
    list_display = ('title', 'user', 'public' ,'created_at')

    #to add a filter
    list_filter = ('public', 'user__username', 'categories__name')

    #creating a hook to save current user
    def save_model(self, request, obj, form, change) :
        print('------------------', obj)
        # obj : this is title of article
        if not obj.user_id :
            obj.user_id = request.user.id
        
        obj.save()

#registering models in Administration Panel
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
