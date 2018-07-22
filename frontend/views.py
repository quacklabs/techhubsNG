from django.shortcuts import render

# Create your views here.


def index(request):
    text = {
        "title" : "Home",
        "text": "this is the home page" 
    }
    return render(request, "frontend/home.html", text)

def login(request):
    ctx = {
        "title": "login"
    }
    return render(request, "frontend/login.html", ctx)

def handler404(request):
    return render(request, 'frontend/404.html', status=404)

def handler500(request):
    return render(request, 'frontend/500.html', status=500)