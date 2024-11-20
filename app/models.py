from django.db import models

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
    
