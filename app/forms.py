from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from .models import Event




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