from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterUser

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account for {username} created successfuly!')
            return redirect('instagram:index')
        
    else:
        form=RegisterUser()
    return render(request,'registration/register.html',{'form':form})
