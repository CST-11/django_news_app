from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime
# Create your views here.


current_date = str(datetime.datetime.now().date())
api_key = "f1ba48fe4a0a469bac55c7f5ec5a5d85"

def home(request):
    keyword = str(request.GET.get('keyword'))
    search_HK_news_url = "https://newsapi.org/v2/everything?q="+keyword+"&from="+current_date+"&sortBy=relevancy&apiKey="+api_key+""
    HK_news_mention_keyword = requests.get(search_HK_news_url).json()

    a = HK_news_mention_keyword['articles']
    source = []
    author = []
    url = []
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        if "hk" in f["url"]:
            source.append(f['source']['name'])
            author.append(f['author'])
            title.append(f['title'])
            url.append(f['url'])
            desc.append(f['description'])
            img.append(f['urlToImage'])
    mylist = zip(source, author, title, url, desc, img)
    context = {'mylist': mylist}

    return render(request, 'search_HK_news/home.html', context)


