from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Author (models.Model):
    name = models.CharField (max_length= 200)
    join_date = models.DateTimeField()
    details = models.CharField(max_length= 500)

    def __str__ (self):
        return self.name

class BlogPost (models.Model):
    title = models.CharField (max_length= 200)
    author = models.ForeignKey (Author, on_delete= models.CASCADE)
    pub_date = models.DateTimeField()
    blog_text = models.CharField (max_length = 10000)

    def __str__  (self):
        return self.title

class Comments (models.Model):
    blog = models.ForeignKey (BlogPost, on_delete= models.CASCADE)
    commentor = models.CharField (max_length = 200)
    comment_text= models.CharField (max_length= 1000)

    def __str__ (self):
        return self.comment_text
