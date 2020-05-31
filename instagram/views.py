from django.shortcuts import render,redirect,get_object_or_404
from .forms import NewImage
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comments
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
@login_required
def index(request):
    images=Image.objects.order_by('-posted')
    return render(request,'instagram/index.html',{'images':images})

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

@login_required
def comment(request,image_id):
    image=Image.objects.get(pk=image_id)
    comments=Image.get_comments(image_id)
    is_liked=False
    if image.likes.filter(id=request.user.id):
        is_liked=True
    return render(request, 'instagram/comment.html',{'image':image,'comments':comments,'is_liked':is_liked})


def likes(request):
    image=get_object_or_404(Image,pk=request.POST.get('image_id'))
    is_liked=False
    if image.likes.filter(id=request.user.id):
        image.likes.remove(request.user)
        is_liked=False
    else:
        image.likes.add(request.user)
        is_liked=True
    return HttpResponseRedirect(reverse('instagram:comment', args=(image.id,)))