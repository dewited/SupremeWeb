from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import upcoming_release
from django.template import loader
from bs4 import BeautifulSoup
import urllib
# Create your views here.

url_to_scrape = 'http://www.supremenewyork.com/previews/fallwinter2016'

def soup():
    soup = BeautifulSoup(urllib.urlopen(url_to_scrape))
    articles = soup.findAll('article')
    base_address = "https://supremenewyork.com/"
    address = []
    for i in articles:
        address_2 = i.find('a')['href']
        address.append(base_address + address_2)
    return address

def main(request):
    supreme_selection = upcoming_release.objects.all()
    context = {'supreme_selection' : supreme_selection}
    return render(request, 'supreme/main.html', context )

def releases(request):
    return HttpResponse("Releases")

def details(request, object_id):
    supremed = get_object_or_404(supreme_selection, pk = object_id)
    return render(request, 'supreme/details', {'supreme_selection':supremed})

def users(request):
    return HttpRequest("Users")
