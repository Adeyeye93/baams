from django.shortcuts import render, redirect, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

def sign_up(req):

    if req.method == "POST":
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['pass']

        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user is not None:
            auth_login(req, login_user)
            return redirect('Recycles')
        else:
            return redirect('register')
    return render(req, "users/index.html")


def login(req):

    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['pass']
        
        login_user = authenticate(username=username, password=password)
        if login_user is not None:
            auth_login(req, login_user)
            return redirect('Recycles')
        else:
            return redirect('login')
    return render(req, "users/login.html")
