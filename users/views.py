from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

#Used for the registeration process
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home-index')
        else:
            print('Inside but wrong')
    else:
        form = UserCreationForm()
    return render(request, 'home/register.html', {'form': form})

def logout_view(request):
    logout(request) #Builtin function to logout user
    context = RequestContext(request)
    # Redirect to a success page.
    return redirect('home-index')