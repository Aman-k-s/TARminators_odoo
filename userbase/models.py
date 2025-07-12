from django.db import models
from django.contrib.auth.models import User

class userbase(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=128)
    public = models.BooleanField(default=True)
    profileImg = models.ImageField(upload_to="user_profile/", null=True, blank=True)
    joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
