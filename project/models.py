from django.db import models
from main.models import Mainfolio

# Create your models here.
class Projectfolio(models.Model):
    user = models.ForeignKey(Mainfolio, blank=False, on_delete=models.CASCADE,related_name='project')
    project_name = models.CharField(max_length=50,blank=False)
    project_description = models.TextField(max_length=60,blank=False)
    project_link = models.URLField(blank=False)
    project_image = models.URLField(blank=True,null=True,default='https://libum.vercel.app/assets/linktree-features-analytics.webp')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name

class blog(models.Model):
    user = models.ForeignKey(Mainfolio, blank=False, on_delete=models.CASCADE,related_name='blog')
    title = models.CharField(max_length=100,blank=False)
    post = models.TextField(max_length=20000,blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title