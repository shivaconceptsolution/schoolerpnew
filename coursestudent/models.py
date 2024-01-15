from django.db import models

class Course(models.Model):
    coursename = models.CharField(max_length=50)
    def __str__(self):
        return self.coursename
class Student(models.Model):
    name = models.CharField(max_length=50)
    fees = models.IntegerField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " " + str(self.fees) + " " + self.course.coursename
class Job(models.Model):

    jobtitle = models.CharField(max_length=100)

    jobdescription = models.CharField(max_length=500)

