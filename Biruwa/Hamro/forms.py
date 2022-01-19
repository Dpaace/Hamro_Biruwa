from django import forms
from django.contrib.auth import get_user_model
from django.db.models import fields

User = get_user_model()

class UserResgistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255,required=True) 
    class Meta:
        model = User
        fields = ["username","first_name","last_name","phone_number","email","password","confirm_password"]
        