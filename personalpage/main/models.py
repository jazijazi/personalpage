from django.db import models
from PIL import Image as PilImage

class Personal(models.Model):
    name = models.CharField(max_length=50 , help_text="Enter Your Name")
    role = models.CharField(max_length=50 , help_text="Enter Your role or job")
    image = models.ImageField(default='default.png')

    def save(self, *args, **kwargs):
        super().save(*args , **kwargs)

        img = PilImage.open(self.image.path)
        
        if img.height > 100 or img.width > 100 :
            output_size = (100,100)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Links(models.Model):
    Email     = models.CharField(max_length=100 , blank=True , null=True)
    phone     = models.CharField(max_length=100 , blank=True , null=True)
    website   = models.CharField(max_length=100 , blank=True , null=True)
    linkedin  = models.CharField(max_length=100 , blank=True , null=True)
    github    = models.CharField(max_length=100 , blank=True , null=True)
    gitlab    = models.CharField(max_length=100 , blank=True , null=True)
    facebook  = models.CharField(max_length=100 , blank=True , null=True)
    twitter   = models.CharField(max_length=100 , blank=True , null=True)
    telegram  = models.CharField(max_length=100 , blank=True , null=True)
    instagram = models.CharField(max_length=100 , blank=True , null=True)
    others    = models.CharField(max_length=100 , blank=True , null=True)

class Education(models.Model):
    degree = models.CharField(max_length=100 , help_text="Enter title of degree")
    university = models.CharField(max_length=100 , blank=True , null=True , help_text="Enter you university or ...")
    years = models.CharField(max_length=100 , blank=True , null=True , help_text="Ex: 2010-2014")

class Languages(models.Model):
    language = models.CharField(max_length=100 , help_text="Ex: French")

class Interests(models.Model):
    interest = models.CharField(max_length=100 , help_text="Ex: Climbing")

class CareerProfile(models.Model):
    Career = models.TextField(max_length=1000 , help_text="Enter Your Career Summary")

class Experiences(models.Model):
    title       = models.CharField(max_length=100 )
    company     = models.CharField(max_length=100 , blank=True , null=True)
    years       = models.CharField(max_length=100 , blank=True , null=True , help_text="EX: 2010-2015")
    description = models.TextField(max_length=500 , blank=True , null=True)

class Projects(models.Model):
    name = models.CharField(max_length=100 , help_text="Enter Your Project Name")
    link = models.CharField(max_length=100 , blank=True , null=True , help_text="Enter Your Project Link")
    description = models.TextField(max_length=500 , blank=True , null=True)

class Skills(models.Model):
    name = models.CharField(max_length=100 , help_text="Skills & Proficiency")
    percent = models.IntegerField(default=0 , help_text="Enter Percentage Of This Skill EX:50")

