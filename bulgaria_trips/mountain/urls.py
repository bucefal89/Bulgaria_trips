from django.urls import path
from bulgaria_trips.mountain.views import MountainCreatView, MountainListView, mountain_details, MountainUpdateView, MountainDeleteView

urlpatterns = [
    path('', MountainListView.as_view(), name='list mountains'),
    path('mountain/create/', MountainCreatView.as_view(), name='create mountain'),
    path('mountain/details/<int:pk>', mountain_details, name='details mountain'),
    path('mountain/update/<int:pk>', MountainUpdateView.as_view(), name='update mountain'),
    path('mountain/delete/<int:pk>', MountainDeleteView.as_view(), name='delete mountain'),
    # path('mountain/create/source/', MountainSourceCreatView.as_view(), name='create source'),
]