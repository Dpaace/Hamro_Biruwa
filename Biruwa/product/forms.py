from django import forms
from django.contrib.auth.models import User
from product.models import ReviewRating

#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)


class ReviewForm(forms.ModelForm):
    class Meta:
        model= ReviewRating
        fields=['subject','review',]
                   