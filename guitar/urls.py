"""guitar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from guitarApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomePage.as_view()),
    path('videos', VideosPage.as_view()),
    path('details', Guitardetails.as_view()),
    path('batches', BatchesPage.as_view()),
    path('contact', ContactPage.as_view()),
    path('about', AboutPage.as_view()),
    path('feestructure', feestructurePage.as_view()),
    path('buyguitar', BuyguitarPage.as_view()),

]
