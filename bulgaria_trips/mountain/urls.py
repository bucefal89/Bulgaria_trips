from django.urls import path
from bulgaria_trips.mountain.views import MountainCreatView, MountainListView

urlpatterns = [
    path('', MountainListView.as_view(), name='list mountains'),
    path('mountain/create/', MountainCreatView.as_view(), name='create mountain'),
]