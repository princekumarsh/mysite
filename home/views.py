from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'username':"prince kumar"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.now() )
        contact.save()
        messages.success(request, "Your message has been sent.")
    return render(request,"contact.html")