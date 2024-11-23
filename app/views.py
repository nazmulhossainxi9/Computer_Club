from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login as signins, logout as signsout
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from . import models
import datetime
from django.conf import settings
import os
from django.utils.timezone import now
from django.db.models import Q

from django.core.paginator import Paginator
from .models import Event
from .forms import EventForm



# Create your views here.

def home(request):
    committee_folder = os.path.join(settings.STATICFILES_DIRS[0], 'img/committee')
    ec = os.path.join(settings.STATICFILES_DIRS[0], 'img/ec')
    # Get the image file names
    image_files = [f for f in os.listdir(committee_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
    ec_img = [f for f in os.listdir(ec) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Example data: you can modify this to fetch data from a database
    committee_names = [ "Shahriar Manzoor", "Md. Sohel Rana", "Tashrif Mahmud"]
    ec_names = ["Md. Shaneaous Emon", "Md. Nesar Uddin", "Zakia Sultana Srabonti", "Rakibul Hasan Efty"]
    designations = ["Chairman", "Co-ordinator, SEUCC", "Asst. Co-ordinator, SEUCC"]
    ec_designations = ["President", "Vice-President", "General Secratery", "Treasurer"]
    texts = ["Dept. of Computer Science & Engineering", "Lecturer, Dept. of Computer Science & Engineering", "Lecturer, Dept. of Computer Science & Engineering"]
    ec_texts = ["CSE-10", "CSE-60" , "CSE-12", "CSE-51"]

    # Zip the lists and image files together to create the committee data
    committee_data = [
        {
            'name': name,
            'designation': designation,
            'text': text,
            'image': f'img/committee/{image}'
        }
        for name, designation, text, image in zip(committee_names, designations, texts, image_files)
    ]
    ec_data = [
        {
            'name': name,
            'designation': designation,
            'text': text,
            'image': f'img/ec/{image}'
        }
        for name, designation, text, image in zip(ec_names, ec_designations, ec_texts, ec_img)
    ]
    events = Event.objects.all().order_by('-created_at')
    return render(request, "html/home.html", {'committee_data': committee_data, 'ec_data': ec_data, 'events': events})


# Signup 
def signup(request):
    form = forms.SignupForm()
    if request.user.is_authenticated:
        return HttpResponseRedirect("home")
    else:
        if request.method == "POST":
            form = forms.SignupForm(request.POST)
            if form.is_valid():
                # Extract user data
                username = form.cleaned_data["username"]
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                email = form.cleaned_data["email"]
                password1 = form.cleaned_data["password1"]
                password2 = form.cleaned_data["password2"]
                if password1 == password2:

                    user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password1)
                    user.save()
                    messages.success(request, "Signup successful! Please log in.")
                    return HttpResponseRedirect("login")  # Redirect to signin after signup
                else:
                    messages.warning(request, "Passowrd Doesn't Matched")
                    return HttpResponseRedirect("signup")
            else:
                messages.warning(request, "Signup failed. Please correct the errors below.")
        return render(request, "html/signup.html", {"form": form})


# Login 
def login(request):
    data = forms.LoginForm()
    next_url = request.GET.get('next')

    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            data = forms.LoginForm(request=request, data=request.POST)
            if data.is_valid():
                username = data.cleaned_data["username"]
                password = data.cleaned_data["password"]
                user = authenticate(username = username, password = password)
                if user is not None:
                    signins(request, user)
                    messages.success(request, "Login Successfull")
                    if next_url:
                        return redirect("{}".format(next_url))
                    return HttpResponseRedirect("home")
            else:
                messages.warning(request, "Invallied Username or Password")     
        else:
            return render(request, "html/login.html", {"form": data})
    return render(request, "html/login.html", {"form": data})


# Logout 
def logout(request):
    if request.user.is_authenticated:
        signsout(request)
        messages.warning(request, "You Have Logged Out")
        return HttpResponseRedirect("home")
    else:
        return HttpResponseRedirect("login")
    



def events(request):
    form = EventForm()
    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'POST':
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('events')
        else:
            events = Event.objects.all().order_by('-created_at')
            paginator = Paginator(events, 6)  # 6 events per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'html/events.html', {
                'page_obj': page_obj,
                'form': form,
                'user_can_create': request.user,
            })
    else:
        events = Event.objects.all().order_by('-created_at')
        paginator = Paginator(events, 6)  # 6 events per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'html/events.html', {
            'page_obj': page_obj,
            'user_can_create': request.user,
        })
    





def members(request):
    form = forms.MembersForm()

    # Get the current year
    current_year = now().year

    # Check if the user has selected a year, default to the current year if not
    selected_year = request.GET.get('year')
    if not selected_year:
        selected_year = current_year  # Default to current year if no year is provided
    else:
        selected_year = int(selected_year)  # Convert to integer if provided

    # Filter members based on the selected year
    members = models.Members.objects.filter(joining_year=selected_year)

    # Grouping members by position
    position_groups = {
        'Elected Committee': members.filter(position__in=['President', 'Vice President', 'GS', 'Treasurer']),
        'Graphics Design': members.filter(position='Graphics Design'),
        'Research Team': members.filter(position='Research Team'),
        'General Member': members.filter(position='General Member'),
    }

    # For staff or superusers, handle member creation and viewing
    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'POST':
            form = forms.MembersForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'html/members.html', {
                'form': form,
                'position_groups': position_groups,
                'selected_year': selected_year,
                'years': models.Members.objects.values_list('joining_year', flat=True).distinct().order_by('joining_year'),
                'is_admin': True,
            })
        return render(request, 'html/members.html', {
            'form': form,
            'position_groups': position_groups,
            'selected_year': selected_year,
            'years': models.Members.objects.values_list('joining_year', flat=True).distinct().order_by('joining_year'),
            'is_admin': True,
        })

    # For regular users
    return render(request, 'html/members.html', {
        'position_groups': position_groups,
        'selected_year': selected_year,
        'years': models.Members.objects.values_list('joining_year', flat=True).distinct().order_by('joining_year'),
        'is_admin': False,
        'current_year': current_year,
    })


def construction(request):
    return render(request, "html/error.html")



def certificate(request):
    form = forms.CertificateForm()
    results = None
    photo_url = None

    if request.method == 'POST' and 'search' in request.POST:
        query = request.POST.get('query')
        # Filter certificates based on user_id or email
        results = models.Certificate.objects.filter(
            Q(user_id=query) | Q(email=query)
        ).order_by('-year')



    elif request.method == 'POST' and 'add_certificate' in request.POST:
        form = forms.CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'html/certificate.html', {
        'form': form,
        'results': results,
    })