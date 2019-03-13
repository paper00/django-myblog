# pylint: disable=no-member
import time
import random
from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from . import models

def main(request):
    articles = models.Article.objects.all()
    username = str(request.user)
    return render(request, 'blog/main.html', {'Articles': articles, 'username': username})

def classify(request, article_category):
    articles = models.Article.objects.all().filter(category=article_category)
    username = str(request.user)
    return render(request, 'blog/classify.html', {'Articles': articles, 'username': username})

def article_page(request, article_id):
    # Judge authority
    article = models.Article.objects.get(pk=article_id)
    if str(request.user) != str(article.author):
        return render(request, 'blog/article_page.html', {'Article': article, 'state': 0})
    return render(request, 'blog/article_page.html', {'Article': article, 'state': 1})

def edit_page(request, article_id):
    # Post new
    if article_id == '0':
        return render(request, 'blog/edit_page.html')
    # Modify article
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'Article': article})

def edit_action(request):
    # Get from form by method="post"
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    category = request.POST.get('category', 'CATEGORY')
    article_id = request.POST.get('id', '0')

    # Post new
    if article_id == '0':
        author = request.user
        models.Article.objects.create(title=title, author=author, category= category, content=content)
        # View new posting
        article = models.Article.objects.get(title=title)
        return HttpResponseRedirect('/myblog/article_page/' + str(article.id))

    # Modify article
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.category = category
    article.save()
    # View posting
    return HttpResponseRedirect('/myblog/article_page/' + str(article.id))

def delete_action(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    article.delete()
    # Back to main page
    return HttpResponseRedirect('/myblog/main/')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'blog/sign_up.html')
    if request.method == 'POST':
        user_id = request.POST.get('username')
        user_pw = request.POST.get('password')
        User.objects.create_user(username = user_id, password = user_pw)
        user = auth.authenticate(username=user_id, password=user_pw)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = user_id
            return render(request, 'blog/login_state.html', {'state': 1, 'user_name': user_id})
        else:
            return render(request, 'blog/login_state.html', {'state': 0})

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'blog/sign_in.html')
    else:
        user_id = request.POST.get('username')
        user_pw = request.POST.get('password')
        # parse here
        user = auth.authenticate(username=user_id, password=user_pw)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = user_id
            return render(request, 'blog/login_state.html', {'state': 1, 'user_name': user_id})
        else:
            return render(request, 'blog/login_state.html', {'state': 0})

def login_state(request):
    return render(request, 'blog/login_state.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    # Back to main page
    return HttpResponseRedirect('/myblog/main/')