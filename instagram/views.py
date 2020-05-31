from django.shortcuts import render,redirect,get_object_or_404
from .forms import NewImage,NewComment,UpdateUser,UpdateProfile
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comments
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

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
def update_profile(request):
    if request.method=="POST":
        user_update=UpdateUser(request.POST,instance=request.user)
        profile_update=UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
        if user_update.is_valid() and profile_update.is_valid():
            user_update.save()
            profile_update.save()
            
            messages.success(request,f'Updated Successfully!')
            return redirect('instagram:profile')
        
    else:
        user_update=UpdateUser(instance=request.user)
        profile_update=UpdateProfile(instance=request.user.profile)
    return render(request,'instagram/update.html',{'user_update':user_update,'profile_update':profile_update})


@login_required
def comment(request,image_id):
    image=Image.objects.get(pk=image_id)
    comments=Image.get_comments(image_id)
    is_liked=False
    if image.likes.filter(id=request.user.id):
        is_liked=True
        
    current_user=request.user
    if request.method=='POST':
        form=NewComment(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.image=image
            comment.user=current_user
            comment.save()  
            
    else:
        form=NewComment() 
    return render(request, 'instagram/comment.html',{'image':image,'comments':comments,'is_liked':is_liked, 'form':form})


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


def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term=request.GET.get('search')
        searched=User.objects.filter(username=search_term)
        message=f'{search_term}'
        
        return render(request, 'instagram/search.html', {'searches':searched,'message':message})
    
    else:
        message='Search not found!'
        return render(request,'instagram/search',{'message':message})
        
        
#VIEW FOR A PARICULAR IMAGE USER
def post_user(request, user_id):
    user=User.objects.get(pk=user_id)
    return render(request,'instagram/image_user.html',{'user':user})