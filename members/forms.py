from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from django.db.models.base import Model
from django.forms import fields, widgets
from members.accountStatus import ACCOUNT_STATUS

from members.models import Profile
from .countries import COUNTRIES


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class ProfileForm(forms.ModelForm):
    phoneNumber = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    country = forms.ChoiceField(choices=COUNTRIES, widget=forms.Select(attrs={'class':'form-control'}))


    class Meta:
        model = Profile
        fields = ('phoneNumber', 'country')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['phoneNumber'].label = "Phone Number:"