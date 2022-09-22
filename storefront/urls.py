"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls')),
    path('news-scraping/bs', include('core.urls')),
    path('HK_newsheadline', include('HK_newsheadline.urls'), name= 'HK_newsheadline'),
    path('foreign_media_newsheadline', include('foreign_media_newsheadline.urls'), name='foreign_media_newsheadline'),
    path('search_HK_news', include('search_HK_news.urls'), name='search_HK_news'),
    path('search_major_foreign_media_news', include('search_major_foreign_media_news.urls'),name='search_major_foreign_media_news')
]
