from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Bruger model used as "customer" for the website
class Bruger(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(blank=True, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    # replace the object string name with the name field of the object insted
    def __str__(self):
        return self.name

# Husreglerform used for the rule part
class Husreglerform(models.Model):
    text = models.TextField(max_length=2000, null=True)
    
    # replace the object string name with the id of the object insted
    def __str__(self):
        return str(self.id)

# Infoform used for the info field 
class Infoform(models.Model):
    text = models.TextField(max_length=2000, null=True)
   
    # replace the object string name with the id of the object insted
    def __str__(self):
        return str(self.id)
    
# news feed model showing user who made the news and what the message is
class Senestenyt(models.Model):
    bruger = models.ForeignKey(Bruger, on_delete=models.SET_NULL, null=True)
    besked = models.TextField(max_length=1000, null=True)

    # replace the object string name with the bruger of that object insted
    def __str__(self):
        return str(self.bruger)

# this model is used for the (ide part) showing the idea
class Blogpost(models.Model):
    title = models.CharField(max_length=1000, null=True)
    bruger = models.ForeignKey(Bruger, on_delete=models.SET_NULL, null=True)
    postdate = models.DateTimeField(auto_now_add=True, null=True)
    blog_picture = models.CharField(max_length=1000, null=True)
    blog_text = models.CharField(max_length=1000, null=True)

     # replace the object string name with the title field in the object
    def __str__(self):
        return str(self.title)

# this model is used as the comment field for the blogpost 
class Blogcomment(models.Model):
    blog = models.ForeignKey(Blogpost, on_delete=models.SET_NULL, null=True)
    bruger = models.ForeignKey(Bruger, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(max_length=200, null=True)
    postdate = models.DateTimeField(auto_now_add=True, null=True)

    # replace the object string name with the bruger of that object insted
    def __str__(self):
        return str(self.bruger)