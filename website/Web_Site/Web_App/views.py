# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, '/home/zero/Desktop/Github/Ituka/website/Web_Site/Web_App/Web_AppTemps/Web_App/home.html')


def about(request):
    return render(request, '/home/zero/Desktop/Github/Ituka/website/Web_Site/Web_App/Web_AppTemps/Web_App/about.html')


def accounts(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        print("Login Unsuccessful")


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = utils.get_query(query_string, ['title', 'body',])
        posts = Post.objects.filter(entry_query).order_by('created')
        return render(request, 'search.html', { 'query_string': query_string, 'posts': posts })
    else:
        return render(request, 'search.html', { 'query_string': 'Null', 'found_entries': 'Enter a search term' })


