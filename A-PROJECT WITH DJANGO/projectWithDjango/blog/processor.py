
from blog.models import Category, Article

def get_categories(request) :


    # ======================================= doing subqueries in django

                                                                        # flat = True : to get in flat format
    categories_in_use = Article.objects.filter(public = True).values_list('categories', flat = True)

                                    # id__in = categories_in_use  :  to get categories whose id is being used in categories_in_use; it was posible thanks to __ 
    categories = Category.objects.filter(id__in = categories_in_use).values_list('id', 'name', )
    
    return {
        'categories': categories,
        'ids':categories_in_use
    }
