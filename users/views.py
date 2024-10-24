from django.shortcuts import render, redirect, redirect
from django.contrib.auth import authenticate, login as auth_login
from users.models import CustomUser as User
from django.contrib import messages
from django.db import IntegrityError

def sign_up(req):
    if req.method == "POST":
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['pass']

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(req, 'Error - Username already exists')
            return redirect('register')  # Redirect back to register page

        if User.objects.filter(email=email).exists():
            messages.error(req, 'Error - Email already in use')
            return redirect('register')  # Redirect back to register page

        try:
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
                messages.error(req, 'Error - Unable to authenticate user')
                return redirect('register')
        except IntegrityError:
            messages.error(req, 'Error - Unable to create account')
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
