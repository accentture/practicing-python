from django.shortcuts import render

from .models import Page

#importing decorators of django: a decorator is executed previously to the main function
from django.contrib.auth.decorators import login_required



@login_required(login_url = 'login') #with this decortator login always will be required to access to any page

#need to get only a page from database
def page(request, slug) : # slug is obligatory parameter
    
    # query 
    page = Page.objects.get(slug = slug)

    return render(request, 'pages/pages.html', {
        'page' : page
    })