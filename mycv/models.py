from django.db import models


# Create your models here.
class About(models.Model):
    profile_img=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    gmail=models.EmailField(max_length=59)
    description=models.TextField()
    linkedinlink=models.CharField(max_length=80)
    githublink=models.CharField(max_length=80)
    twitterlink=models.CharField(max_length=80)
    facebooklink=models.CharField(max_length=80)
    fiverlink=models.CharField(max_length=80)
    cv_upload=models.FileField(null=True)


class Experience(models.Model):
    designation=models.CharField(max_length=50)
    organization_name=models.CharField(max_length=50)
    description=models.TextField()
    start_date=models.DateField()
    end_date=models.CharField(default="Present",max_length=50)    
    
class Education(models.Model):
    instituate_name=models.CharField(max_length=50)
    degree_name=models.CharField(max_length=50)
    course_name=models.TextField()
    start_date=models.DateField()
    end_date=models.CharField(default="Present", max_length=50) 
    
class Interest(models.Model):
    interst=models.CharField(max_length=200, null=True)
    
# class Contacts(models.Model):
    
class Skill(models.Model):
    skill_name=models.CharField(max_length=50)
    skill_percent=models.IntegerField()
    
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
    
class Project(models.Model):
   project_video=models.FileField(null=True)
   project_name=models.CharField(max_length=200)
   project_description=models.TextField()
   project_link=models.CharField(max_length=200,null=True) 