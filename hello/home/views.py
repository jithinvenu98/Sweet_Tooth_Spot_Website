from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact
from django.contrib import messages
# Create your views here.

def index(request):

    context = {
        'variable1':"i'm B a T M a N",
        'variable2':"i'm S U P E R  M a N  as well "
    }

    messages.success(request,"this is test msg")

    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about")

def options(request):
    return render(request,'options.html')
    #return HttpResponse("this is options")

def contact_view(request):

    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        new_contact = contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        new_contact.save()
        messages.success(request, "your msg has been sent - happie,happie,happie")

    return render(request,'contact.html')



