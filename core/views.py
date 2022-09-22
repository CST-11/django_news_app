from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def news_scraping_BS (keyword):
    myList_BS = [{"media": "MingPao", "url": "https://news.mingpao.com/ins/%E5%8D%B3%E6%99%82%E6%96%B0%E8%81%9E/main",
                  "main_url": "https://news.mingpao.com/"},
                 {"media": "RTHK", "url": "https://news.rthk.hk/rthk/ch/latest-news.htm", "main_url": ""},
                 {"media": "星島 港聞",
                  "url": "https://std.stheadline.com/realtime/hongkong/%E5%8D%B3%E6%99%82-%E6%B8%AF%E8%81%9E",
                  "main_url": ""},
                 {"media": "星島 中國",
                  "url": "https://std.stheadline.com/realtime/china/%E5%8D%B3%E6%99%82-%E4%B8%AD%E5%9C%8B",
                  "main_url": ""},
                 {"media": "HK01 主頁", "url": "https://www.hk01.com/", "main_url": "https://www.hk01.com"},
                 {"media": "HK01 社會新聞",
                  "url": "https://www.hk01.com/channel/2/%E7%A4%BE%E6%9C%83%E6%96%B0%E8%81%9E",
                  "main_url": "https://www.hk01.com"},
                 {"media": "HK01 政情", "url": "https://www.hk01.com/channel/310/%E6%94%BF%E6%83%85",
                  "main_url": "https://www.hk01.com"},
                 {"media": "HKET", "url": "https://topick.hket.com/srat006/%E6%96%B0%E8%81%9E",
                  "main_url": "https://topick.hket.com"},
                 {"media": "EJ", "url": "https://www2.hkej.com/instantnews/current",
                  "main_url": "https://www2.hkej.com/"},
                 {"media": "AM730 港聞", "url": "https://www.am730.com.hk/%E6%9C%AC%E5%9C%B0",
                  "main_url": "https://www.am730.com.hk"},
                 {"media": "中通社", "url": "http://www.hkcna.hk/index_col.jsp?channel=2804",
                  "main_url": "http://www.hkcna.hk/"}]
    from bs4 import BeautifulSoup as bs
    import requests
    import re
    search_results = []
    for k in range(len(myList_BS)):
        search_results.append("\n" + myList_BS[k]['media'] + ">>>>")
        result = requests.get(myList_BS[k]['url'] )
        soup = bs(result.content, "html.parser")

        list_of_tag_title = soup.find_all("a",attrs={"title" : re.compile(keyword)})
        list_of_tag = soup.find_all("a",string=re.compile(keyword))
        news_dict = {}
        for i in range(len(list_of_tag_title)):
            news_dict.update({"News title "+str(i+1)+"" : list_of_tag_title[i]["title"]})
            if not list_of_tag_title[i]['href'].startswith("https://"):
                news_dict.update({"News url "+str(i+1)+"" : myList_BS[k]['main_url'] +list_of_tag_title[i]["href"]})
            else:
                news_dict.update({"News url "+str(i+1)+"" : list_of_tag_title[i]["href"]})

        for i in range(len(list_of_tag)):
            news_dict.update({"News title "+str(i+1)+"" : list_of_tag[i].string})
            if not list_of_tag[i]['href'].startswith("https://"):
                news_dict.update({"News url "+str(i+1)+"" : myList_BS[k]['main_url'] +list_of_tag[i]["href"]})
            else:
                news_dict.update({"News url "+str(i+1)+"" : list_of_tag[i]["href"]})

        temp = {val: key for key, val in news_dict.items()}
        removed_duplicates = {val: key for key, val in temp.items()}
        i=1
        for value in removed_duplicates.values():
            if (i%2)== 0:
                search_results.append('{}\n'.format(value))
                search_results.append("\n")
            else:
                search_results.append('{}\n'.format(value))
            i = i+1
        search_results.append("<<<<")
    return search_results


def home(request):
    search_results_dict= {}
    key_for_dict = []
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        search_results = news_scraping_BS(keyword)
        number_of_result = len(search_results)
        for k in range(number_of_result):
            key_for_dict.append(str("result"+ str(k)))
        search_results_dict = dict(zip(key_for_dict, search_results))
        pass
    return render(request, 'core/home.html', {'search_results_dict': search_results_dict})




