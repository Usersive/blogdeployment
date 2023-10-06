from django.db import models

# Create your models here.
class Courses(models.Model):
    course_heading = models.CharField(max_length=30)
    course_link = models.CharField(max_length=100)
    course_notes = models.TextField(max_length=600)
    image = models.ImageField(upload_to='images/')

    
   
    
    def __str__(self):
        return f'Courses heading: {self.course_heading} Course Note:{self.course_notes}'

class Service(models.Model):
    service_icon = models.CharField(max_length = 20)
    service_heading = models.CharField(max_length=50)
    service_note = models.TextField(max_length=200)
    
    def __str__(self):
        return self.service_heading
    
