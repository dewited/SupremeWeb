"""supremebot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'supreme'

urlpatterns = [
    url(r'^$', views.main, name = 'main'),
    url(r'^releases/$', views.releases, name = 'releases'),
    url(r'^details/(?P<object_id>[0-9]+)/$', views.details, name = 'details'),
    url(r'^users/$', views.user_info, name = 'user_info'),
    ]
