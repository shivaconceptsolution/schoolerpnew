from django.shortcuts import render
from .models import Course,Student,Job
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse
class JobCreate(CreateView):
    model = Job
    fields = ['jobtitle', 'jobdescription']
    success_url='/coursestudent/'
class JobList(ListView):
    model = Job   # Job.objects.all()   
'''def index(request):
    coursedata = Course.objects.all()
    return render(request,"coursestudent/course.html",{"c":coursedata})'''
def stuinfo(request,id):
    studentdata = Student.objects.filter(course_id=id)
    return render(request,"coursestudent/student.html",{"st":studentdata})
def studetailinfo(request,id):
    studata = Student.objects.get(pk=id)
    return render(request,"coursestudent/detail.html",{"dt":studata})
'''def fileupload(request):
    if request.method=="POST":
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fileinfo = fs.save(myfile.name, myfile)
        filepath = fs.url(fileinfo)
        return render(request,"coursestudent/fileupload.html",{"key":filepath})
    return render(request,"coursestudent/fileupload.html")'''

def ajaxload(request):
    return render(request,"coursestudent/ajaxsearch.html")

def ajaxdata(request):
    param = request.GET["q"]
    record=Student.objects.filter(name__contains=param)
    return render(request,"coursestudent/ajaxresult.html",{'key':record})

def ajaxjquery(request):
    return render(request,"coursestudent/ajaxjquery.html")

def ajaxjquerycode(request):
    c=Course(coursename=request.POST.get("coursename"))
    c.save()
    return HttpResponse("data inserted successfully")

