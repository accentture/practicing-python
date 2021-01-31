from django.shortcuts import render

from .models import Page
# Create your views here.

#need to get only a page from database
def page(request, slug) : # slug is obligatory parameter
    
    # query 
    page = Page.objects.get(slug = slug)

    return render(request, 'pages/pages.html', {
        'page' : page
    })