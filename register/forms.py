from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterUser(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(RegisterUser,self).__init__(*args,**kwargs)
        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text=None
            
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']