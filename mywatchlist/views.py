from django.core import serializers
from django.shortcuts import render, HttpResponse
from mywatchlist.models import WatchList

# Create your views here.

data_mywatchlist = WatchList.objects.all()
context = {
    'mywatchlist' : data_mywatchlist
}

def show_mywatchlist(request):
    return render(request, 'mywatchlist.html', context)

# make xml and json format
def show_mywatchlist_xml(request):
     return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")


def show_mywatchlist_json(request):
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")