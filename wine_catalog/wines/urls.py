from django.urls import path
from wines.views import WineListView, WineDetailView, ContactView

app_name = 'wines'

urlpatterns = [
    path('', WineListView.as_view(), name='wine_list'),
    path('wines/<slug:slug>/', WineDetailView.as_view(), name='wine_detail'),
    path('contacts/', ContactView.as_view(), name='contact'),
]
