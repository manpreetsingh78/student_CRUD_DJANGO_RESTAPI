from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ("Full Stack Developer", "Full Stack Developer"),
)

class Student_Data(models.Model):
    #Alphanumeric student ID, Full Name, address, email address and guardian's name
    student_id = models.CharField(max_length=100,blank=False,null=False,unique=True)
    full_name = models.CharField(max_length=255,blank=False,null=False)
    address = models.TextField(max_length=1000,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    guardian_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Student_Score(models.Model):
    #alphanumeric student ID, student name, course name, year in which the exam is conducted.
    studentid = models.ForeignKey(Student_Data,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255,default='Full Stack Developer',choices=STATUS_CHOICES)
    scores = models.TextField(max_length=1000,blank=False,null=False)
    yearofexam = models.IntegerField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


#-------------------JWT AUTH----------------

# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
#     if created:
#         Token.objects.create(user=instance)
