from django.http.response import HttpResponse
from django.shortcuts import render
from notebook.models import Contact
from django.contrib import messages



# Create your views here.
def notebook(request):
    context={
        "hii":"i am new now"
    }
    messages.info(request, 'this is for test')
    return render(request,"home.html",context)

    #return HttpResponse("Notebook")
def home(request):
    return render(request,"home.html")
def home1(request):
    return render(request,"home1.html")
    #return HttpResponse("hey i am home page")

def contact(request):
    if request.method=="POST":
        name =request.POST.get("name")
        email =request.POST.get("email")

        models=Contact(name=name,email=email)
        models.save()
        messages.success(request, 'Profile details updated.')

    return render(request, "contact.html")

    #return HttpResponse("9960512466")
def about(request):
    return render(request, "about.html")
    #return HttpResponse("tell me something about you")
def services(request):
    return render(request, "services.html")
    #return HttpResponse("tell me whats your problem")