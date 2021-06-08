from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    return render(request, 'users/dashboard.html')

def register(request):
    if request.method == "GET":
        return render(request, "users/register.html",{"form": CustomUserCreationForm})
    elif request.method == "POST":
        try:
            user_exists = User.objects.get(username=request.POST['username'])
            return render(request, "users/username_exists.html")
        except User.DoesNotExist:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
            return redirect(reverse("dashboard"))

