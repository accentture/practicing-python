# ====================================== este fichero es el controlador (view)

from django.shortcuts import render, HttpResponse, redirect # importando HttpResponse
                                                # redirect : to redirect


#importing my models
from miapp.models import Article

# it allows to use OR in a filter
from django.db.models import Q
# Create your views here.

# importing class to work with forms in django
from miapp.forms import FormArticle

#to use flash messages
from django.contrib import messages

""" 
    --diferneicas entre un MVC y MVT
    --MVC = modelo vista controdor
    --MVT = modelo template vista 
        --en django la vista = template
        --en django controlador = view
 """

layout = """
    <h1>Sitio web con django</h1>
    <hr>
    <ul>
        <li>
            <a href="/inicio" >Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo" >Hola mundo</a>
        </li>
        <li>
            <a href="/pagina-pruebas" >Pagina pruebas</a>
        </li>
        <li>
            <a href="/contacto-dos" >Contacto</a>
        </li>
    <ul>

"""

#el metodo index es la página de inicio
def index(request) :
    """
    html = ""
        <h1>Pagina principal con Django</h1>
        <p>Años hasta el 2050</p>
        <ul>
    ""
    year = 2021
    while year <= 2040 :
        if year % 2 == 0 :
            html += f"<li>{str(year)}</li>"
        year += 1


    html += "</ul>"
    """
    year = 2021
    until = range(year, 2051)

    name = 'Jonathan Alejandro'
    languages = ['JavaScript', 'Python', 'PHP', 'C']

    #return HttpResponse(layout + html)
    #ussing render method to charge our templates
    #to use it allows to evit spaguetty code
    return render(request, 'index.html', {
        #passing data to the template
        "title" : 'Inicio 2',
        'my_variable' : 'Soy un dato que esta en la vista',
        'name':name,
        'languages': languages,
        'years': until
    })


             #la request permitira recibir parametros cuando se haga peticiones a una url
def hola_mundo(request) :
#usar guión bajo como convención

    #haciendo respuesta http usando HttpResponse
    #para que esto funcione debo de cargarlo en una url ,ir al packege principal  ->  urls
    #return HttpResponse(layout +"""
    #    <h1>Hola mundo con Django</h1>
    #    <h3>Soy Alejandro</h3>
    #""")

    #using render
    return render(request, 'hola_mundo.html')

def pagina(request, to_redirect = 0) : # is important to set a value by default

    if to_redirect == 1 :

        #redirect to inicio page
        #return redirect('/inicio/')

        #adding params
        #return redirect('/contacto/jonathan/diaz')

        #more complex redirection, using page and adding params
                                    #it is a clean way to pass params
        return redirect('contacto', nombre="jonathan", apellidos="mollocondo")
                        #name of route


    return render(request, 'pagina.html', {
        'text':'',
        'list':['uno', 'dos', 'tres']
    })

def contacto(request, nombre = "", apellidos = "") :
    html = ""
    if nombre and apellidos :
        html += "<p>El nombre completo es<p>"
        html += f"{nombre} {apellidos}"

    return HttpResponse(layout + f"<h2>Contacto</h2>" + html)

                #passing params from url
def create_article(request, title, content, public) :
    article = Article(
        title = title, #if I delete this param, mi article equal will be created in my database
        content = content,
        public = public
    )

    #saving article in database
    article.save()

    return HttpResponse(f"Article created: <strong>{article.title}</strong> - {article.content}")


# method to get article
def article(request) :

    try:
                            # params for get are fields of my model, for example : id, pk, title
                            # title="cuarto titulo" : it is as WHERE in MySQL
                            # , public=False : it is like AND
        article = Article.objects.get(title="cuarto titulo", public=True) # objects : it allows accessing to model, to that objects
        response = f"Articulo: {article.id} - {article.title}"
                                        # get : it always need a param  to get a specific register

    except:
        response = '<h1>Articulo no encontrado</h1>'

    return HttpResponse(response)

#to update article
def edit_article(request, id_article) :
    article = Article.objects.get(pk=id_article)

    article.title = "Batman"
    article.content = "Peliculas del 2017"
    article.public = True

    article.save()

    return HttpResponse(f"Articulo editado: {article.id} - <strong>{article.title}</strong> - {article.content}")

#to diplay articles
def articles(request) :
    # it is recomendable to work with ORM of Django, because if we want to change other SGBD, equally will work, for example with SQLite, MySQL, PostgreSQL

    articles = Article.objects.order_by('id') # all() : it allows to get many register of database
                                          # order_by() : it is sql clausule, it allows order according whatever, params are field of model
                                          # -title : this param order in inverse way
                                          # [:3] : it limit number of elements to be showed
                                          # [2:5] : it set range of elements


                                    # doing multiple conditionals
    articles = Article.objects.filter(title='Batman', id=5) # filter() : this method allows to put conditionals


    # ================ the next are LOOKUPS with FILTERS
    articles = Article.objects.filter(id__lte=8, title__icontains="articulo") 
                                    
                                    # title__contains="articulo" : this means title that contains "articulo" 
                                    # title__exact="articulo" :  this means title that is exact to "articulo" 
                                    # title__iexact="articulo": it has not casesentive, that is to say that doesn't difference between uppercase and loweercase
                                    # id__gt=8 : it means greater than  > 8
                                    # id__gte=8 : it means greater equal >= 8 
                                    # id__lte=8 : it means less equal than  > 8

    articles = Article.objects.filter(
                                    title__contains="Articulo"

                                ).exclude( # exclude : it excludes items
                                    public=True
                                )

    # ================ raw queries of SQL with Django
    articles = Article.objects.raw("SELECT * FROM miapp_article WHERE title = 'Articulo 9' AND public=0 ")

    
    # ================ using OR
    articles = Article.objects.filter(
        Q(title__contains="2") | Q(title__contains="3") | Q(title__contains="4") #  |  : it acts as OR
    )

    articles = Article.objects.all().order_by('-id')

    articles = Article.objects.filter(public = True).order_by('id')  

    return render(request, 'articles.html', {
        'articles': articles
    })


def delete_article(request, id) :
    article = Article.objects.get(pk=id)
    article.delete()

    return redirect('articles')

def save_article_with_form(request) :

    # checking if arrives data through GET or POST, but is better use POST because the information will be more sure. When I use POST, I am using headers of request and the information never will be visible
    if request.method == 'POST' :

        #collect data by GET or POST
        title = request.POST['title']

        if len(title) < 5 : 
            return HttpResponse('<h2>Error. El titulo es muy pequeño</h2>')

        content = request.POST['content']
        public = request.POST['public']

        article = Article(
            title = title, #if I delete this param, mi article equal will be created in my database
            content = content,
            public = public
        )

        #saving article in database
        article.save()

        return HttpResponse(f"Article created: <strong>{article.title}</strong> - {article.content}")
    else : 
        return HttpResponse('<h2>No se ha podido crear el articulo</h2>')


#to use with form
def create_article_with_form(request) : 
    return render(request, 'create template with forms.html')

def create_article_with_classes_based_in_django(request) : 

    # checking if there are data by 'POST'
    if request.method == 'POST' :
        form = FormArticle(request.POST) # after to pass data, it will clean data, will try valite information

        # checking if form is valid
        if form.is_valid() :
            
            #collecting data
            data_form = form.cleaned_data # cleaned_data : these are clean data that arrive

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']
            
            # saving article in database
            article = Article(
                title = title, #if I delete this param, mi article equal will be created in my database
                content = content,
                public = public
            )

            article.save()

            #creating flash message ( this message only will be displayed once)
            messages.success(request, f"Has creado correctamente el artículo {article.id}")

            #return HttpResponse(article.title + ' - ' + article.content + ' - ' + str(public))
            return redirect('articles')

    else : 
        # empty form
        form = FormArticle()

    return render(request, 'create forms based in classes.html', {
        'form': form
    })
