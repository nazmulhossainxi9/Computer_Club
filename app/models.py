from django.db import models
import os
from multiselectfield import MultiSelectField
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




def profile_photo_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"apply_profile_photos/{instance.student_code}.{ext}"




# class ClubJoinRequest(models.Model):
#     # Choices for departments
#     DEPARTMENT_CHOICES = [
#         ('CSE', 'CSE'),
#         ('Pharmacy', 'Pharmacy'),
#         ('EEE', 'EEE'),
#         ('Textile', 'Textile'),
#         ('Architecture', 'Architecture'),
#         ('Bangla', 'Bangla'),
#         ('English', 'English'),
#         ('Economics', 'Economics'),
#         ('LLB', 'LLB'),
#         ('BBA', 'BBA'),
#     ]

#     # Choices for skills and interests
#     SKILL_CHOICES = [
#         ('graphics_design', 'Graphics Design'),
#         ('video_editing', 'Video Editing'),
#         ('motion_graphics', 'Motion Graphics'),
#         ('competitive_programming', 'Competitive Programming'),
#         ('web_development', 'Web Development'),
#         ('android_development', 'Android Development'),
#         ('e_sports', 'E-Sports'),
#         ('ui_ux_design', 'UI/UX Design'),
#         ('event_management', 'Event Management'),
#         ('content_writing', 'Content Writing'),
#         ('photography', 'Photography'),
#         ('paper_crafting', 'Paper Crafting'),
#         ('volunteering', 'Volunteering'),
#         ('singing', 'Singing'),
#         ('dancing', 'Dancing'),
#         ('anchoring', 'Anchoring'),
#         ('debating', 'Debating'),
#         ('other', 'Other'),
#     ]

#     BLOOD_GROUP_CHOICES = [
#         ('A+', 'A+'),
#         ('A-', 'A-'),
#         ('B+', 'B+'),
#         ('B-', 'B-'),
#         ('O+', 'O+'),
#         ('O-', 'O-'),
#         ('AB+', 'AB+'),
#         ('AB-', 'AB-'),
#     ]

#     # Basic information
#     university_email = models.EmailField(unique=True)
#     full_name = models.CharField(max_length=150)
#     student_code = models.CharField(max_length=20, unique=True)
#     department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, default="CSE")
#     batch = models.CharField(max_length=10)
#     semester = models.CharField(max_length=10)
#     current_cgpa = models.FloatField()
#     personal_email = models.EmailField()
#     personal_contact_number = models.CharField(max_length=15)
#     emergency_contact_number = models.CharField(max_length=15)
#     present_address = models.TextField()
#     permanent_address = models.TextField()
#     blood_group = models.CharField(max_length=15, choices=BLOOD_GROUP_CHOICES, default="")

#     # Skills and interests
#     skills = MultiSelectField(choices=SKILL_CHOICES, blank=True)
#     interests = MultiSelectField(choices=SKILL_CHOICES, blank=True)

#     # Club-related questions
#     # experience_in_organization = models.BooleanField(default=False)
#     experience_details = models.TextField(blank=True, null=True)
#     # attached_to_other_clubs = models.BooleanField(default=False)
#     other_clubs_details = models.TextField(blank=True, null=True)

#     # Agreement to club rules
#     agree_meeting_attendance = models.BooleanField(
#         default=False,
#         help_text="I will attend 80% of the club meetings"
#     )
#     agree_program_participation = models.BooleanField(
#         default=False,
#         help_text="I will not miss Two(2) consecutive programs."
#     )
#     agree_to_truthfulness = models.BooleanField(
#         default=False,
#         help_text="I will be truthful to Club Moderators and other members"
#     )
#     agree_to_respectfulness = models.BooleanField(
#         default=False,
#         help_text="I will be respectful to my Faculties and senior students"
#     )
#     agree_to_behavior = models.BooleanField(
#         default=False,
#         help_text="I will be helpful and won't behave rudely to my junior studentsr"
#     )
#     agree_to_tools_usage = models.BooleanField(
#         default=False,
#         help_text="I am able to use Viber and What's App on my mobile phone. I am using mobile data along with Wi-Fi on my phone."
#     )
#     agree_to_disciplinary_rules = models.BooleanField(
#         default=False,
#         help_text="I will not leave SEUCC without the permission of the Executive Committee"
#     )
#     agree_to_general_member_terms = models.BooleanField(
#         default=False,
#         help_text="I will not be involved in any undisciplined activities. If I do so I will accept any punishment taken against me."
#     )

#     # joined_messenger_group = models.BooleanField(default=False)
#     facebook_profile_link = models.URLField(max_length=300, blank=True, null=True)
#     profile_photo = models.ImageField(upload_to=profile_photo_upload_path, blank=True, null=True)

#     def __str__(self):
#         return f"{self.full_name} ({self.student_code})"
    





class ApplyClub(models.Model):
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
    SKILL_CHOICES = [
        ('graphics_design', 'Graphics Design'),
        ('video_editing', 'Video Editing'),
        ('motion_graphics', 'Motion Graphics'),
        ('competitive_programming', 'Competitive Programming'),
        ('web_development', 'Web Development'),
        ('android_development', 'Android Development'),
        ('e_sports', 'E-Sports'),
        ('ui_ux_design', 'UI/UX Design'),
        ('event_management', 'Event Management'),
        ('content_writing', 'Content Writing'),
        ('photography', 'Photography'),
        ('paper_crafting', 'Paper Crafting'),
        ('volunteering', 'Volunteering'),
        ('singing', 'Singing'),
        ('dancing', 'Dancing'),
        ('anchoring', 'Anchoring'),
        ('debating', 'Debating'),
        ('other', 'Other'),
    ]

    student_code = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, default="CSE")
    batch = models.CharField(max_length=10, default="")
    university_email = models.CharField(max_length=100, default="")
    personal_email = models.CharField(max_length=100, default="")
    blood_group = models.CharField(max_length=100, choices=BLOOD_GROUP_CHOICES, default="Blood Group")
    facebook_link = models.CharField(max_length=300, default="")
    image = models.ImageField(upload_to='ClubJoinRequest/', default='default.jpg')
    
    semester = models.CharField(max_length=10, default=None)
    current_cgpa = models.FloatField(null=True, blank=True, default=None)
    
    personal_contact_number = models.CharField(max_length=15, default="")
    emergency_contact_number = models.CharField(max_length=15, default="")
    
    present_address = models.TextField(default="")
    permanent_address = models.TextField(default="")    

    # skills = MultiSelectField(choices=SKILL_CHOICES, blank=True)
    # interests = MultiSelectField(choices=SKILL_CHOICES, blank=True)

    experience_details = models.TextField(blank=True, null=True, default="")
    other_clubs_details = models.TextField(blank=True, null=True, default="")
    agree_meeting_attendance = models.BooleanField(
        default=False,
        help_text="I will attend 80% of the club meetings"
    )
    agree_program_participation = models.BooleanField(
        default=False,
        help_text="I will not miss Two(2) consecutive programs."
    )
    agree_to_truthfulness = models.BooleanField(
        default=False,
        help_text="I will be truthful to Club Moderators and other members"
    )
    agree_to_respectfulness = models.BooleanField(
        default=False,
        help_text="I will be respectful to my Faculties and senior students"
    )
    agree_to_behavior = models.BooleanField(
        default=False,
        help_text="I will be helpful and won't behave rudely to my junior studentsr"
    )
    agree_to_tools_usage = models.BooleanField(
        default=False,
        help_text="I am able to use Viber and What's App on my mobile phone. I am using mobile data along with Wi-Fi on my phone."
    )
    agree_to_disciplinary_rules = models.BooleanField(
        default=False,
        help_text="I will not leave SEUCC without the permission of the Executive Committee"
    )
    agree_to_general_member_terms = models.BooleanField(
        default=False,
        help_text="I will not be involved in any undisciplined activities. If I do so I will accept any punishment taken against me."
    )

        # joined_messenger_group = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name
