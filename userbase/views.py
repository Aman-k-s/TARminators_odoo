from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error(None, "Invalid username or password.")

    return render(request, "login.html", {"form": form})

def logoutUser(request):
    logout(request)
    return redirect("/login")

def signupUser(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})