from django.shortcuts import render, redirect, redirect
from django.contrib.auth import authenticate, login as auth_login
from users.models import CustomUser as User
from django.contrib import messages

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
            messages.success(req, 'Success - You are Signed-In')

            next_url = req.GET.get('next')
            if next_url:
                return redirect(next_url)  # Redirect to the 'next' page if available
            else:
                return redirect('Recycles')  # Default redirection if 'next' is not provided
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
            messages.success(req, 'Success - You are Logged-In')
            next_url = req.GET.get('next')
            if next_url:
                return redirect(next_url)  # Redirect to the 'next' page if available
            else:
                return redirect('Recycles')  # Default redirection if 'next' is not provided
        else:
            messages.error(req, 'Wrong credentials')
            return redirect('login')

    return render(req, "users/login.html")
