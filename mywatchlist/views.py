from django.core import serializers
from django.shortcuts import render, HttpResponse
from mywatchlist.models import WatchList

# Create your views here.

data_mywatchlist = WatchList.objects.all()

def show_banyak_nonton(request):
    total_movies = data_mywatchlist.count()
    total_watched = WatchList.objects.filter(watched=True).count()
    context = {
         'banyak_nonton': total_watched>=total_movies
    }
    return render(request, 'message.html', context)

def show_mywatchlist(request):
    
    context = {
        'mywatchlist' : data_mywatchlist,
       
    }
    return render(request, 'mywatchlist.html', context)

# make xml and json format
def show_mywatchlist_xml(request):
     return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")


def show_mywatchlist_json(request):
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

