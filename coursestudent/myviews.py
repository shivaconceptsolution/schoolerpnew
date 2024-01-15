from django.views import View
from django.shortcuts import render
from .models import Course,Student
from django.conf import settings
from django.core.files.storage import FileSystemStorage
class Welcome(View):
    def get(self,request):
        coursedata = Course.objects.all()
        return render(request,"coursestudent/course.html",{"c":coursedata})

class Fileupload(View):
    def get(self,request):
        return render(request,"coursestudent/fileupload.html")
    def post(self,request):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fileinfo = fs.save(myfile.name, myfile)
        filepath = fs.url(fileinfo)
        return render(request,"coursestudent/fileupload.html",{"key":filepath})    