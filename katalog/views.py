from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

data_barang_wishlist = CatalogItem.objects.all()
context = {
    'list_katalog': data_barang_wishlist,
    'name': 'Catherine',
    'student_id': '2106705392'
}

def show_catalog(request):
    return render(request, "katalog.html", context)
