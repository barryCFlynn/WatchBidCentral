from django import forms
from buy.models import Listing

class CreateListing(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'