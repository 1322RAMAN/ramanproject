from django import forms
from user.models import UserRegistration

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        exclude = ["first_name","last_name","email","password","active","verify_link","log_in_time","log_out_time"]