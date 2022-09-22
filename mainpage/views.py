from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.

def mainpage(request):
    return render(request, 'mainpage/mainpage.html')

def HK_newsheadline(request):
    return render(request, 'HK_newsheadline/home.html')

def foreign_media_newsheadline(request):
    return render(request, 'foreign_media_newsheadline/home.html')

def search_HK_news(request):
    return render(request, 'search_HK_news/home.html')

def search_major_foreign_media_news(request):
    return render(request, 'search_major_foreign_media_news/home.html')