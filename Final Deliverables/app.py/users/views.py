from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, models
from . forms import CreateUserForm, Aboutforms, Quoteform
from django.contrib import messages
from . models import Members, Office


# Create your views here.


def register(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)


def loginpage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'registration/login.html', context)

def logoutusers(request):
    logout(request)
    return redirect('login')
    
@login_required(login_url='login')
def index(request):
    form = Aboutforms()
    if request.method =='POST':
        form = Aboutforms(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thank You for your subscription')
            return redirect('index')

    context = {'form':form}   
    return render(request, 'index.html', context)

@login_required(login_url='login')
def contact(request):
    context = {}
    return render(request,'contact.html', context)

@login_required(login_url='login')
def products(request):
    context = {}
    return render(request, 'products.html', context)


@login_required(login_url='login') 
def services(request):
    context = {}
    return render(request, 'service.html', context)
@login_required(login_url='login')
def about(request):
    context = {}
    return render(request, 'about.html', context)

def quote(request):
    form = Quoteform()
    if request.method =='POST':
        form = Quoteform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thankyou for your valuable feedback')

    context = {'form': form}
    return render(request, 'quoteform.html', context)

def landing_page(request):
    context = {}
    return render(request, 'landingpage.html', context)
    