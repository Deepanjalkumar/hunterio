from django.shortcuts import redirect, render, HttpResponse
import requests
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):

    context = {}
    if request.method=="POST":
        try:
            domain=request.POST['domain']
            r=requests.get(f"http://localhost:8000/email/{domain}")
            data=r.json()[f"{domain}"]
            context = {
                'email': data
            }
        except Exception as e:

            context = {
                'email': "Not found"
            }

    return render(request, "website/index.html", context)

def domain_search(request):
    return render(request, "website/domain_search.html")

def email_finder(request):
    return render(request, "website/email_finder.html")

def author_finder(request):
    return render(request, "website/author_finder.html")

def email_verifier(request):
    return render(request, "website/email_verifier.html")

def pricing(request):
    return render(request, "website/pricing.html")

def blog(request):
    return render(request, "website/blog.html")

def templa(request):
    return render(request, "website/templa.html")

def help_center(request):
    return render(request, "website/help_center.html")

def about_us(request):
    return render(request, "website/about_us.html")

def our_data(request):
    return render(request, "website/our_data.html")

def careers(request):
    return render(request, "website/careers.html")

def loginuser(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/loginuser") 
        
    return render(request, "website/login.html")




