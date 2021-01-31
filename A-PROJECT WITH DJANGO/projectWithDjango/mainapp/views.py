from django.shortcuts import render, redirect

#to make flash messages, where a flash message only appear one time
from django.contrib import messages

#importing module of authentication
from django.contrib.auth.forms import UserCreationForm

#importing my form
from .forms import RegisterForm

# Create your views here.
def index(request) :
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def about(request) :
    return render(request, 'mainapp/about.html', {
        'title': 'Sobre nosotros'
    })

def register_page(request) :
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




