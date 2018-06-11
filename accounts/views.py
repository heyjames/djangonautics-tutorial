# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Instance with email, pw, etc
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm() # Blank instance

    return render(request, 'accounts/signup.html', { 'form':form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # It is named with "data" because it is not naturall the first parameter of this function
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST: # "next" refers to the <input name="next"... part of HTML.
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', { 'form':form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
