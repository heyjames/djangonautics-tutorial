# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})

@login_required(login_url="/accounts/login/") # This is a decorator that extends the function and adds additional functionality.
def article_create(request):
    if request.method == 'POST': # If POST, pass the data to forms.CreateArticle() in the line below
        form = forms.CreateArticle(request.POST, request.FILES) # When we upload files, we get it separately on "FILES"
        if form.is_valid():
            # save article to db.
            instance = form.save(commit=False) # "commit=False" is basically saying: hang on, we're going to save in a bit, but don't commit to the action. Just give me the instance we're about to save and we'll do something with it and then you can save.
            instance.author = request.user # "author" comes from the articles/model.py
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()

    return render(request, 'articles/article_create.html', { 'form':form })
