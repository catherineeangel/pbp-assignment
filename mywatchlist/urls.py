
from django.urls import path

from mywatchlist.views import show_mywatchlist, show_mywatchlist_json, show_mywatchlist_xml, show_banyak_nonton
# from katalog.views import show_catalog

app_name = 'mywatchlist' 

urlpatterns = [
    path('', show_banyak_nonton, name='show_banyak_nonton'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json')
]