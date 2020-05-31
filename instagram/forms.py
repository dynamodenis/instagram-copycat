from .models import Images,Comments,Profile
from django import forms
from django.contrib.auth.models import User

class NewImage(forms.ModelForm):
    class Meta:
        model=Images
        fields=['image_caption','image']
        
class NewComment(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=['image','user','likes']
        
        
class UpdateUser(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']
        
class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','picture']