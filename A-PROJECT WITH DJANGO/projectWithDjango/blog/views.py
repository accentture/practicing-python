from django.shortcuts import render, get_object_or_404

#to make pagination
from django.core.paginator import Paginator

from blog.models import Article, Category

# Create your views here.
def list(request) : #request is data of petition

    articles = Article.objects.all()

    #paginate articles
    paginator = Paginator(articles, 1) #first param is the list that I want to paginate
                                      #second param is the number of elements that I want for page

    #to pick page that will arrive throught URL
    page = request.GET.get('page')

    #to save all articles that the page arrived
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_articles
    })

def category(request, category_id) :

    #category = Category.objects.get(id = category_id)

    #creating page 404
                            #passing as params Category and a condition
    category = get_object_or_404(Category, id = category_id)

    #getting articles that belong it specific category
    articles = Article.objects.filter(categories = category_id) #it is possible to pass other param as  category,  and it will work equally

    return render(request, 'categories/category.html', {

        # when use {}, it is named context
        'category': category,

    })

def article(request, article_id) :
    article = get_object_or_404(Article, id = article_id)

    return render(request, 'articles/detail.html', {
        'article': article
    })


