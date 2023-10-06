from django.db import models

# Create your models here.
class Subscribe(models.Model):
    name = models.CharField(max_length= 200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=600)
    
    
    
    def __str__(self):
        return f'Name:   {self.name}     Email: {self.email}'
