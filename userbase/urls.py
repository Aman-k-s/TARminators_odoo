from django.urls import path
from userbase import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('signup/', views.signupUser, name='signup'),
    path('profile/', views.profile_view, name='profile'),

]