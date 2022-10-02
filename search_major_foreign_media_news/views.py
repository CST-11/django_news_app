from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime
# Create your views here.


current_date = str(datetime.datetime.now().date())
api_key = "f1ba48fe4a0a469bac55c7f5ec5a5d85"


def home(request):
    keyword = str(request.GET.get('keyword'))
    search_major_foreign_media_news_url = "https://newsapi.org/v2/everything?domains=bloomberg.com,reuters.com,bbc.co.uk,wsj.com,washingtonpost.com,cnn.com,cnbc.com,apnews.com,aljazeera.com&q="+keyword+"&from="+current_date+"&sortBy=relevancy&apiKey="+api_key+""
    major_foreign_media_news_mention_keyword = requests.get(search_major_foreign_media_news_url).json()

    a = major_foreign_media_news_mention_keyword['articles']
    source = []
    author = []
    url = []
    desc = []
    title = []
    img = []

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

    return render(request, 'search_major_foreign_media_news/home.html', context)

'''
    keyword = "&q="+str(request.GET.get('keyword'))
    list_of_source_code = ["REUTERS", "bbc-news", "bloomberg", "the-wall-street-journal", "the-washington-post", "CNN", "associated-press", "al-jazeera-english"]
    source = []
    author = []
    url = []
    desc = []
    title = []
    img = []

    for source_code in list_of_source_code:
        search_major_foreign_media_news_url = "https://newsapi.org/v2/everything?sources="+source_code+""+keyword+"&from="+current_date+"&sortBy=relevancy&apiKey="+api_key+""
        major_foreign_media_news_mention_keyword = requests.get(search_major_foreign_media_news_url).json()
        a = major_foreign_media_news_mention_keyword['articles']
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
'''