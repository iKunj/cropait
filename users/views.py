from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

#Used for the registeration process
def register(request):
    form  = UserCreationForm()
    return render(request, 'home/register.html', {'forms':form}) #Custom forms can be defined over the default django provided forms

def logout_view(request):
    logout(request) #Builtin function to logout user
    context = RequestContext(request)
    # Redirect to a success page.
    return redirect('home-index')