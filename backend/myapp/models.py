from django.db import models

# Create your models here.
class Project(models.Model):
    tite = models.CharField(max_length=200)
    script = models.FileField('/scripts', null=True, blank=True)
    createor_note = models.TextField()
    link = models.URLField(blank=True, null=True)
    password_access = models.BooleanField(default=False)
    comprabale_titles = models.TextField()
    access_password = models.CharField(max_length=128, blank=True) 