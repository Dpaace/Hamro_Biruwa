from django import forms
from django.contrib.auth import get_user_model
from django.db.models import fields

User = get_user_model()

class UserResgistrationForm(forms.ModelForm):
    # confirm_password = forms.CharField(max_length=255,required=True) 
    class Meta:
        model = User
        fields = ["username","first_name","last_name","phone_number","email","password"]
        widgets = {
            'password': forms.PasswordInput()
        }

    def get_id(self):
        return self.user.id

class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','first_name', 'last_name', 'email', 'password']
#         widgets = {
#             'password': forms.PasswordInput()
#         }
