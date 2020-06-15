from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bruger(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(blank=True, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Husreglerform(models.Model):
    text = models.TextField(max_length=2000, null=True)
    
    def __str__(self):
        return str(self.id)
    
class Infoform(models.Model):
    text = models.TextField(max_length=2000, null=True)
   
    def __str__(self):
        return str(self.id)
    
class Senestenyt(models.Model):
    bruger = models.ForeignKey(Bruger, on_delete=models.SET_NULL, null=True)
    besked = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return str(self.bruger)

class Blogcomment(models.Model):
    bruger = models.ForeignKey(Bruger, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(max_length=200, null=True)
    postdate = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.bruger)

class Blogpost(models.Model):
    title = models.CharField(max_length=1000, null=True)
    bruger = models.ForeignKey(Bruger, on_delete=models.SET_NULL, null=True)
    postdate = models.DateTimeField(auto_now_add=True, null=True)
    blog_picture = models.CharField(max_length=1000, null=True)
    blog_text = models.CharField(max_length=1000, null=True)
    blogcomment = models.ManyToManyField(Blogcomment, blank=True)

    def __str__(self):
        return str(self.title)