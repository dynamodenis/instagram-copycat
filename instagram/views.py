from django.shortcuts import render,redirect,get_object_or_404
from .forms import NewImage
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comments

# Create your views here.

def index(request):
    return render(request,'instagram/index.html')

@login_required
def new_image(request):
    current_user=request.user
    if request.method=='POST':
        form=NewImage(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('instagram:index')
    
    else:
        form=NewImage()
        
    return render(request, 'instagram/image.html',{'form':form})

@login_required
def profile(request):
    return render(request,'instagram/profile.html')