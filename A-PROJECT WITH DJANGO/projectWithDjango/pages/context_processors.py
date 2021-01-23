""" this file work like the views, but after I will be able to use in differents places """

"""     
        ** context_processors
            -- a context procesor is an option that allows to have information in all my templates                -- I need to create other conext processor here, it allows to charge all my pages in this context processor and to access to this context processor from whatever part of my project
            --in this case I need to display in my menu that is contained in _layout.html


        ** auth : object authentication
            --where I have all auth, debug and messages in all my templates
"""


from pages.models import Page 

def get_pages(request) :

    #using a query to database
                                                        # flat = True : to get a flat text
    pages = Page.objects.values_list('title', flat = True) # values_list() : it allows select one element that I want to display, in this case it method allow me get three values (id, title, slug)

    return {
        'pages': pages
    }



