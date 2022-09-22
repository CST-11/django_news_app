from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def home(request):
    api_key = "f1ba48fe4a0a469bac55c7f5ec5a5d85"
    url = "https://newsapi.org/v2/top-headlines?country=hk&apiKey=" + api_key

    Hongkong_news_headlines = requests.get(url).json()

    a = Hongkong_news_headlines['articles']
    source = []
    author = []
    url = []
    desc =[]
    title =[]
    img =[]

    for i in range(len(a)):
        f = a[i]
        source.append(f['source']['name'])
        author.append(f['author'])
        title.append(f['title'])
        url.append(f['url'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(source, author, title, url, desc, img)

    context = {'mylist': mylist}

    return render(request, 'HK_newsheadline/home.html', context)
