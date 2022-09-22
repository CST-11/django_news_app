from django.shortcuts import render
from django.http import HttpResponse
import requests
#
# # Create your views here.

def home(request):
    api_key = "f1ba48fe4a0a469bac55c7f5ec5a5d85"

    source =[]
    author =[]
    url =[]
    desc =[]
    title =[]
    img =[]

    list_of_source_code = ["REUTERS", "bbc-news", "bloomberg", "the-wall-street-journal", "the-washington-post", "CNN", "associated-press", "al-jazeera-english"]
    for source_code in list_of_source_code:
        request_url = "https://newsapi.org/v2/top-headlines?sources=" + source_code + "&apiKey=" + api_key
        foreign_media_newsheadline = requests.get(request_url).json()
        a = foreign_media_newsheadline['articles']
        for i in range(3):
            f = a[i]
            source.append(f['source']['name'])
            author.append(f['author'])
            title.append(f['title'])
            url.append(f['url'])
            desc.append(f['description'])
            img.append(f['urlToImage'])

    mylist = zip(source, author, title, url, desc, img)
    context = {'mylist': mylist}

    return render(request, 'foreign_media_newsheadline/home.html', context)
