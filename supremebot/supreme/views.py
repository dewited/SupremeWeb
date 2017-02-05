from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import upcoming_release, users
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
    new_user = users()
    new_user.first_name = request.POST['first_name']
    new_user.last_name = request.POST['last_name']
    new_user.email = request.POST['email']
    new_user.credit_card_num = request.POST['credit_card_num']
    new_user.shipping_address = request.POST['shipping_address']
    new_user.address = request.POST['address']
    new_user.card_maker = request.POST['card_maker']
    new_user.save()
    return render(request, 'supreme/releases.html',{'user_info' : new_user })

def details(request, object_id):
    supremed = get_object_or_404(upcoming_release, pk = object_id)
    return render(request, 'supreme/details.html', {'supreme_selection':supremed})

def user_info(request):
    user_context = get_object_or_404(users, pk = 1)
    return render (request, 'supreme/user_info.html', {'user_selection' : user_context})
