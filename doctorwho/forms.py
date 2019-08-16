from django import forms
from .models import Complication,Feedback,Profile


class LetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')


class ComplicationForm(forms.ModelForm):
    class Meta:
        model = Complication
        fields = ('complication_name', 'symptoms')
        exclude = ['pub_date']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('feedback',)
        exclude = ['pub_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'image', 'contact')
        exclude = ['pub_date']

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)