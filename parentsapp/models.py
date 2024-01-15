from django.db import models
class Register(models.Model):

 emailid= models.CharField(max_length=200)  

 password= models.CharField(max_length=200)

 mobile= models.CharField(max_length=200)

 fullname= models.CharField(max_length=200)
 def __str__(self):
    return self.emailid + " " + self.password + " " + self.mobile + " " + self.fullname

class Course(models.Model):
   coursename = models.CharField(max_length=20)
   fees = models.IntegerField()
   branchname=models.CharField(max_length=20)
   duration = models.IntegerField()
   def __str__(self):
      return self.coursename + " ," + str(self.fees)

class Contact(models.Model):
   name = models.CharField(max_length=50)
   phoneno = models.CharField(max_length=12)
   email = models.CharField(max_length=150)
   message = models.CharField(max_length=50)
   def __str__(self):
      return "name is "+str(self.name) + " phone no "+str(self.phoneno) + " email " + self.email + " " + self.message