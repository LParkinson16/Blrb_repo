from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(req):
    """Register new user accounts"""
    if req.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=req.POST)
        if form.is_valid():
            new_user = form.save()
            login(req, new_user)
            return redirect('blrb_app:index')
    path = 'registration/register.html'
    context = {'form':form}
    return render(req, path, context)
