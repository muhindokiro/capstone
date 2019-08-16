from django.shortcuts import render,redirect
import datetime as dt
from .forms import RegisterForm,ComplicationForm,FeedbackForm,ProfileForm,LetterForm
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .email import send_welcome_email
from .models import Complication,Feedback,Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

# Index view.
@login_required(login_url='/accounts/login/')
def index(request):
    # bizna = Bussiness.objects.all()
    complication = Complication.objects.all()
    feedback = Feedback.objects.all()
    form = ComplicationForm(request.POST, request.FILES)
    form1 = FeedbackForm(request.POST, request.FILES)
    return render(request, 'index.html', {"complication":complication,"feedback":feedback,"form": form,"form1": form1})

# Profile view.
@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.profile()
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            send_welcome_email(name,email)
            HttpResponseRedirect('profile')
    else:
        form = LetterForm()
    return render(request, 'profile.html', {"profile":profile,"letterForm":form})

# New_complication view.
@login_required(login_url='/accounts/login/')
def new_complication(request):
    # complication = Complication.index()
    current_user = request.user
    if request.method == 'POST':
        form = ComplicationForm(request.POST, request.FILES)
        if form.is_valid():
            complication = form.save(commit=False)
            complication.save()
        return redirect('index')
    else:
        form = ComplicationForm()
    return render(request, 'new_complication.html', {"form": form})

def feedback(request):
    # feedback = Feedback.index()
    current_user = request.user
    if request.method == 'POST':
        form1 = FeedbackForm(request.POST, request.FILES)
        if form1.is_valid():
            feedback = form1.save(commit=False)
            feedback.save()
        return redirect('index')
    else:
        form1 = FeedbackForm()
    return render(request, 'feedback.html', {"form1": form1})

# Register view.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data['email']
            send_welcome_email(username,email)
            return redirect('index.html')
    else:
        form =RegisterForm()
    return render(request,'registration/registration_form.html',{'form':form})

def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    # Returning the actual day of the week
    day = days[day_number]
    return day


# Search view.
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'complication' in request.GET and request.GET["complication"]:
        search_term = request.GET.get("complication")
        searched_complications = Complication.search_by_complication_name(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"complications": searched_complications})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


# About Us view.
@login_required(login_url='/accounts/login/')
def aboutus(request):
    return render(request, 'aboutus.html')
