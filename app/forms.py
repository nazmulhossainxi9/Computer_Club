from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from .models import Event, Members, Certificate, ApplyClub




class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image', 'details']

    # Manually add widgets with class attributes
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0 border-bottom',
        'placeholder': 'Event Title'
    }))
    
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'form-control border-0 border-bottom',
        'placeholder': 'Choose Event Image'
    }))
    
    details = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control border-0 border-bottom',
        'placeholder': 'Event Details',
        'rows': 4
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        labels = {
            "email": "Email Address",
            "password1": "Password",
            "password2": "Confirm Password",
        }
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Student Code",
            }),
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name",
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "University Email Address",
            }),
             "password1": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Password",
            }),
            "password2": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })





class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        
        # Override the username widget to include placeholder and class
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'autofocus': True,  # Django usually includes this, but good to specify
        })
        
        # Override the password widget to include placeholder and class
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        })


class MembersForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = '__all__'
        widgets = {
            'member_id': forms.TextInput(attrs={
                'placeholder': 'Enter Member ID',
                'class': 'form-control',
            }),
            'student_code': forms.TextInput(attrs={
                'placeholder': 'Enter Student Code',
                'class': 'form-control',
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Full Name',
                'class': 'form-control',
            }),
            'department': forms.Select(attrs={
                'class': 'form-select',
            }),
            'joining_year': forms.NumberInput(attrs={
                'placeholder': 'Enter Joining Year',
                'class': 'form-control',
            }),
            'leaving_year': forms.NumberInput(attrs={
                'placeholder': 'Enter Leaving Year',
                'class': 'form-control',
            }),
            'batch': forms.TextInput(attrs={
                'placeholder': 'CSE 44/CSE D4',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter Email',
                'class': 'form-control',
            }),
            'blood_group': forms.Select(attrs={
                'class': 'form-select',
            }),
            'position': forms.Select(attrs={
                'class': 'form-select',
            }),
            'facebook_link': forms.URLInput(attrs={
                'placeholder': 'Enter Facebook Profile Link',
                'class': 'form-control',
            }),
            'linkedin_link': forms.URLInput(attrs={
                'placeholder': 'Enter LinkedIn Profile Link',
                'class': 'form-control',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.label = ""  # Remove labels



class CertificateSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by Email Address',
            'class': 'form-control',  # Optional: Add a class for styling
        }),
    )


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['user_id', 'name', 'email', 'batch', 'year', 'event_title', 'event_date', 'position', 'photo']
        widgets = {
            'user_id': forms.TextInput(attrs={'placeholder': 'Student Code', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Personal Email', 'class': 'form-control'}),
            'batch': forms.TextInput(attrs={'placeholder': 'Batch: Ex - CSE 44', 'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Year', 'class': 'form-control'}),
            'event_title': forms.TextInput(attrs={'placeholder': 'Event Title', 'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'position': forms.TextInput(attrs={'placeholder': 'Position (optional)', 'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'multiple': False}),
        }

# class ClubJoinRequestForm(forms.ModelForm):
#     class Meta:
#         model = ClubJoinRequest
#         fields = '__all__'
#         widgets = {
#                 'university_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'University Email Address'}),
#                 'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
#                 'student_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Code'}),
#                 'department': forms.Select(attrs={'class': 'form-select'}),
#                 'batch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Batch (CSE-44)'}),
#                 'semester': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Current Semester'}),
#                 'current_cgpa': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Current CGPA'}),
#                 'personal_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Personal Email Address'}),
#                 'personal_contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Personal Contact Number'}),
#                 'emergency_contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Number'}),
#                 'present_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Present Address'}),
#                 'permanent_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Permanent Address'}),
#                 'blood_group': forms.Select(attrs={'class': 'form-select'}),
#                 'skills': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
#                 'interests': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
#                 'experience_details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'If You Have Experience About Clubbing, Write N/A If Not...'}),
#                 'other_clubs_details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'If You are in Anyother Clubs, Write N/A If Not...'}),
#                 'facebook_profile_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your Facebook Profile Link'}),
#                 'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
#                 'agree_meeting_attendance': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#                 'agree_program_participation': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#                 'agree_to_truthfulness': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#                 'agree_to_respectfulness': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#                 'agree_to_behavior': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#                 'agree_to_tools_usage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#                 'agree_to_disciplinary_rules': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#                 'agree_to_general_member_terms': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#             }
#         labels = {
#                 'agree_meeting_attendance': "I will attend 80% of the club meetings",
#                 'agree_program_participation': "I will not miss Two(2) consecutive programs.",
#                 'agree_to_truthfulness': "I will be truthful to Club Moderators and other members",
#                 'agree_to_respectfulness': "I will be respectful to my Faculties and senior students",
#                 'agree_to_behavior': "I will be helpful and won't behave rudely to my junior studentsr",
#                 'agree_to_tools_usage': "I am able to use Viber and What's App on my mobile phone. I am using mobile data along with Wi-Fi on my phone.",
#                 'agree_to_disciplinary_rules': "I will not leave SEUCC without the permission of the Executive Committee",
#                 'agree_to_general_member_terms': "I will not be involved in any undisciplined activities. If I do so I will accept any punishment taken against me.",
#             }


        

class ClubJoinRequestForm(forms.ModelForm):
    class Meta:
        model = ApplyClub
        fields = '__all__'
        widgets = {
                'student_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Code'}),
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
                'department': forms.Select(attrs={'class': 'form-select'}),
                'batch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Batch (CSE-44)'}),
                'university_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'University Email Address'}),
                'personal_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Personal Email Address'}),
                'blood_group': forms.Select(attrs={'class': 'form-select'}),
                'facebook_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your Facebook Profile Link'}),
                'image': forms.FileInput(attrs={'class': 'form-control'}),
                'semester': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Current Semester'}),
                'current_cgpa': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Current CGPA'}),
                'personal_contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Personal Contact Number'}),
                'emergency_contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Emergency Contact Number'}),
                'present_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Present Address'}),
                'permanent_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Permanent Address'}),
                # 'skills': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
                # 'interests': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
                'experience_details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'If You Have Experience About Clubbing, Write N/A If Not...'}),
                'other_clubs_details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'If You are in Anyother Clubs, Write N/A If Not...'}),
                'agree_meeting_attendance': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'agree_program_participation': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'agree_to_truthfulness': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'agree_to_respectfulness': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'agree_to_behavior': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'agree_to_tools_usage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'agree_to_disciplinary_rules': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'agree_to_general_member_terms': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            }
        labels = {
                'agree_meeting_attendance': "I will attend 80% of the club meetings",
                'agree_program_participation': "I will not miss Two(2) consecutive programs.",
                'agree_to_truthfulness': "I will be truthful to Club Moderators and other members",
                'agree_to_respectfulness': "I will be respectful to my Faculties and senior students",
                'agree_to_behavior': "I will be helpful and won't behave rudely to my junior studentsr",
                'agree_to_tools_usage': "I am able to use Viber and What's App on my mobile phone. I am using mobile data along with Wi-Fi on my phone.",
                'agree_to_disciplinary_rules': "I will not leave SEUCC without the permission of the Executive Committee",
                'agree_to_general_member_terms': "I will not be involved in any undisciplined activities. If I do so I will accept any punishment taken against me.",
            }
        
        
        
        
        
        
        