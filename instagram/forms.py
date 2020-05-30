from .models import Image
from django import forms

class NewImage(forms.ModelForm):
    class Meta:
        model=Image
        fields=['image_caption','image']