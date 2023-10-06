from django.db import models

# Create your models here.

class post_blog(models.Model):
    blog_title = models.CharField(max_length=20)
    blog_heading = models.CharField(max_length=30)
    blog_notes = models.CharField(max_length=50)
    blog_details = models.TextField(max_length=3000)
    blog_image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return f'Blog title: {self.blog_title}'
