from django.shortcuts import render
def home(request):
    return render(request,"teacherapp/home.html")

def aboutus(request):
    return render(request,"teacherapp/about.html")
 

def services(request):
    return render(request,"teacherapp/services.html")
 

def login(request):
    return render(request,"teacherapp/login.html")
 

def contactus(request):
    return render(request,"teacherapp/contact.html")
