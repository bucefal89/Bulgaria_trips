from django.urls import path

from bulgaria_trips.top_places.views import *


urlpatterns = [
    path('', PlaceListView.as_view(), name='list places'),
    path('place/create/', PlaceCreateView.as_view(), name='create place'),
    path('place/details/<int:pk>', places_details, name='details place'),
    # path('place/details/<int:pk>', PlaceDetailsView.as_view(), name='details place'),
    path('place/update/<int:pk>', PlaceUpdateView.as_view(), name='update place'),
    path('place/delete/<int:pk>', PlaceDeleteView.as_view(), name='delete place'),
]