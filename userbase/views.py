from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from .models import userbase, Skill
from .forms import SignupForm, LoginForm, UpdateUserForm
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import SkillSerializer


# Create your views here.
# @api_view(['GET'])
# def skill_suggest_api(request):
#     query = request.GET.get('term', '')
#     skills = Skill.objects.filter(name__icontains=query)[:10]
#     return Response(SkillSerializer(skills, many=True).data)

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def user_skills_api(request):
#     profile = userbase.objects.get(user=request.user)

#     if request.method == 'GET':
#         skills = profile.skills.all()
#         serializer = SkillSerializer(skills, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         # Expected: { "skills": ["Python", "SQL", "React"] }
#         skill_names = request.data.get('skills', [])
#         profile.skills.clear()
#         for name in skill_names:
#             skill, _ = Skill.objects.get_or_create(name=name.strip())
#             profile.skills.add(skill)
#         return Response({'success': True})
    
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

from django.shortcuts import render, redirect
from .models import userbase

def profile_view(request):
    if request.user.is_anonymous:
        return redirect("/login")

    profile = userbase.objects.get(user=request.user)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateUserForm(instance=profile)

    return render(request, 'profile.html', {
        'form': form,
        'current_skills': profile.skills.all(),
    })


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