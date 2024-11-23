from django.db import models
import os
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/')
    details = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Members(models.Model):
    DEPARTMENT_CHOICES = [
        ("CSE", "Computer Science and Engineering"),
        ("Pharmacy", "Pharmacy"),
        ("EEE", "Electrical and Electronic Engineering"),
        ("Textile", "Textile Engineering"),
        ("Architecture", "Architecture"),
        ("Bangla", "Bangla Language and Literature"),
        ("English", "English Language and Literature"),
        ("Economics", "Economics"),
        ("LLB", "Bachelor of Laws"),
        ("BBA", "Bachelor of Business Administration"),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    POSITION_CHOICES = [
        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('Tresarure', 'Tresarure'),
        ('General Secretary', 'General Secretary'),
        ('General Member', 'General Member'),
        ('Graphics Design', 'Graphics Design'),
        ('Research & Development', 'Research & Development'),
    ]

    member_id = models.CharField(max_length=50, default="DefaultID")
    student_code = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, default="CSE")
    joining_year = models.IntegerField(null=True, blank=True)
    leaving_year = models.IntegerField(null=True, blank=True)
    batch = models.CharField(max_length=10, default="")
    email = models.CharField(max_length=100, default="")
    blood_group = models.CharField(max_length=100, choices=BLOOD_GROUP_CHOICES, default="Blood Group")
    position = models.CharField(max_length=100, choices=POSITION_CHOICES, default="Member")
    facebook_link = models.CharField(max_length=100, default="")
    linkedin_link = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='members_photos/', default='default.jpg')

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    # Rename the file based on the email address
    ext = filename.split('.')[-1]
    new_filename = f"{instance.email}.{ext}"  # Renaming the photo to email address with the original extension
    return os.path.join('certificate_photos/', new_filename)


class Certificate(models.Model):
    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    batch = models.CharField(max_length=50)
    year = models.IntegerField()
    event_title = models.CharField(max_length=200)
    event_date = models.DateField()
    position = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)  # Make the photo optional

    def __str__(self):
        return f"{self.name} - {self.event_title} ({self.year})"

    
