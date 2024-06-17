from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def registration(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            username = user_form.cleaned_data.get('username')
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Successfully Registered!")
            return redirect("user_login")
        else:
            messages.success(request, "Invalid details")
            return render(request, "users/register.html", {"form1": user_form, "form2": profile_form})
    user_form = UserRegistrationForm()
    profile_form = UserProfileForm()

    return render(request, "users/register.html", {"form1": user_form, "form2": profile_form})

@login_required
def profileself(request):
    return render(request, "users/profileself.html")

def profile(request, id):
    anyuser = get_object_or_404(User, pk=id)
    return render(request, "users/profile.html", {"anyuser": anyuser})
