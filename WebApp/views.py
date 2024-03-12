from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# view di homepage
def home(request):
    # check to see if logging in
    if request.method == 'POST': #'POST' vuol dire che l'utente sta "postando" la richiesta (ovvero le credenziali per il login)
        username = request.POST['username'] #'username' è il nome che avevamo dato in home.html nel form. il dato inserito sarà chiamato così
        password = request.POST['password'] # come per username
        # AUTHENTICATE
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in. Try again.")
            return redirect('home')
        
    else:
        return render(request,'home.html', {})

#view del logout
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    return render(request,'register.html', {})
