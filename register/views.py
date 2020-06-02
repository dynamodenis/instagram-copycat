from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterUser
from .email import send_welcome_mail

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            # send_welcome_mail(username,email)
            messages.success(request,f'Account for created successfuly! You can login.')
            return redirect('login')
        
    else:
        form=RegisterUser()
    return render(request,'registration/register.html',{'form':form})
