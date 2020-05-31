from .models import Image,Comments
from django import forms

class NewImage(forms.ModelForm):
    class Meta:
        model=Image
        fields=['image_caption','image']
        
class NewComment(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=['image','user','likes']