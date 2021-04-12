from django.shortcuts import render, redirect

#to make flash messages, where a flash message only appear one time
from django.contrib import messages

#importing module of authentication
from django.contrib.auth.forms import UserCreationForm

#importing my form
from .forms import RegisterForm

#importing authentication module
from django.contrib.auth import authenticate, login, logout

def index(request) :

    #to access to user loged
    print('-------------------index -------------------', request.user)
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def about(request) :
    return render(request, 'mainapp/about.html', {
        'title': 'Sobre nosotros'
    })

def register_page(request) :

    # if user is authenticated, always to redirect to index_1
    if request.user.is_authenticated :
        return redirect('index_1')
    
    else :
        register_form = RegisterForm()

        if request.method == 'POST' :
            register_form = RegisterForm(request.POST) # request.POST : passing data of form

            if register_form.is_valid() :
                register_form.save()
                
                #using flash messages
                messages.success(request, 'Te has registrado correctamente')

                return redirect('index_2')

                

        return render(request, 'users/register.html', {
            'title': 'Registro',
            'register_form': register_form
        })


""" this function is named login_page(), so it doesn't interference with methods by default of django """
def login_page(request) :

    if request.user.is_authenticated :
        return redirect('index_1')
    
    else :
        if request.method == 'POST' :
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('index_1')

            else :
                #warning message
                messages.warning(request, 'No te has podido identificar correctamente')

        return render(request, 'users/login.html', {
            'title':'Identifícate'
        })

def logout_user(request):
    logout(request) #automatically logout to user loged
    return redirect('login')




