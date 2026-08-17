from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    return render(request, "dashboard.html")

def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            return redirect("dashboard")

        else:

            return render(
                request,
                "login.html",
                {
                    "error": "Invalid username or password."
                }
            )

    return render(request, 'login.html')

