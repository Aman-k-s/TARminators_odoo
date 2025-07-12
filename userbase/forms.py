from django.contrib.auth.models import User
from django import forms
from .models import userbase

class SignupForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = userbase
        fields = ['location', 'public', 'profileImg']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'public': forms.CheckboxInput(),
            'profileImg': forms.ClearableFileInput(),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        pw = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        if pw != confirm:
            raise forms.ValidationError("Passwords do not match.")

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
    )
