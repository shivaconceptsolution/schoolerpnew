from django.shortcuts import render
from django.http import HttpResponse
import requests
def hello(request):
    response = requests.post('http://127.0.0.1:8000/api/register/',{'username':'ravikumar1234578','password':'Ravi@$12345','email':'ravikumar1237877@gmail.com'})
    tutor = response.json()
    print(tutor)
    if(tutor!=None):
        return HttpResponse("Registration Successfully"+str(tutor))
    else:
        return HttpResponse("Registration not Successfully")
    return render(request,"guestapp/index.html",{'data':tutor})
def login(request):
    response = requests.post('http://127.0.0.1:8000/api/login/',{'username':'ravikumar1234578','password':'Ravi@$12345'})
    tutor = response.json()
    print(tutor)
    request.session["token"]=tutor["token"]
    if(tutor!=None):
        return HttpResponse("login Successfully"+str(tutor))
    else:
        return HttpResponse("login not Successfully")
    return render(request,"guestapp/index.html",{'data':tutor})
def studentinfo(request):
    return render(request,"guestapp/student.html")

def studentoutput(request):
    name =request.GET["txtname"]
    email = request.GET["txtemail"]
    contact = request.GET["txtcontact"]
    address = request.GET["txtaddress"]
    return HttpResponse("name is "+name + " <hr> email is "+email + "<hr> contact  is "+contact + " <hr> address is "+address);
def addition(request):
    return render(request,"guestapp/addition.html")

def additionoutput(request):
    num1 = request.GET["txtnum1"]
    num2 = request.GET["txtnum2"]
    c = int(num1)+int(num2)
    return HttpResponse("Result is "+str(c))
def swap(request):
    return render(request,"guestapp/swap.html")
def swaplogic(request):
    a = request.POST["num1"]
    b = request.POST["num2"]
    a,b = b,a
    return render(request,"guestapp/swapresult.html",{"key1":a,"key2":b,"key":"value a={0} and b={1}".format(a,b)})
    #return HttpResponse("value a= "+a+",b = " + b)

def marksheet(request):
    if request.method=='POST':
        marks = {'PHYSICS':request.POST['txtnum1'],'HINDI':request.POST['txtnum2'],'CHEM':request.POST['txtnum3'],'MATHS':request.POST['txtnum4'],'ENG':request.POST['txtnum5']}
        totalmarks=0
        count=0
        result=''
        for key,value in marks.items():
            if(int(value)<33):
                count+=1
            if(int(value)<0 or int(value)>100):
                result = 'Invalid Marks'
                break
            totalmarks+=int(value)
        else:
          if count==0:
             per=totalmarks/5
             if per>33 and per<45:
                result = "Pass with Third Division and percentage is {0}%".format(per)
             elif per<60:
                result = 'Pass with Second Division and percentage is {0}%'.format(per)
             else:
                result='Pass with first division and percentage is {0}%'.format(per)
          elif count==1:
            result = "Try again you are suppl"
          else:
            result = "Sorry Fail"
        return render(request,"guestapp/result.html",{'key':result,'subjectinfo':marks})

    else:
        return render(request,"guestapp/marksheet.html")

def radioexample(request):
    if request.method=='POST':
        course = request.POST['course']
        return render(request,"guestapp/radioexample.html",{"key":course}) 
    else:
        return render(request,"guestapp/radioexample.html")    
def checkboxexample(request):
    if request.method=='POST':
        course = request.POST.getlist('course')
        s = ""
        for data in course:
            s = s + data + " "
        return render(request,"guestapp/checkboxexample.html",{"key":s}) 
    else:
        return render(request,"guestapp/checkboxexample.html")    
def dropdownlistexample(request):
    if request.method=="POST":
        course = request.POST['ddlcourse']
        return render(request,"guestapp/dropdownlistexample.html",{"key":course})
    else:
        return render(request,"guestapp/dropdownlistexample.html")
def listexample(request):
    if request.method=="POST":
        course = request.POST.getlist('ddllist')
        s=''
        for data in course:
            s=s + data + " "

        return render(request,"guestapp/listexample.html",{"key":course,"res":s})
    else:
        return render(request,"guestapp/listexample.html")

def logout(request):
    del request.session["token"]
    // response = requests.post('http://127.0.0.1:8000/api/logout/',{'token':'ravikumar1234578','password':'Ravi@$12345','email':'ravikumar1237877@gmail.com'})
    return redirect('/')