from django.shortcuts import render
from userbase.models import userbase
# Create your views here.

def dashboard(request):
    users = userbase.objects.filter(public=True).select_related('user').prefetch_related('skills')
    return render(request, 'dashboard.html', {'users': users})
