from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Mainfolio(models.Model):
    user = models.OneToOneField(User, blank=False, on_delete=models.CASCADE,related_name='profiles')
    welcome_image = models.URLField(blank=True)
    welcome_text = models.CharField(max_length=150,blank=False)
    facebook = models.URLField(blank=True,null=True)
    linkliden = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    dribble = models.URLField(blank=True,null=True)
    resume = models.URLField(blank=True,null=True)
    github = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.welcome_text
    @property
    def mail (self):
        email = self.user.email
        return email