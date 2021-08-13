from django.urls import path
from bulgaria_trips.beaches import views
from bulgaria_trips.beaches.views import BeachUpdateView

urlpatterns = [
    path('', views.all_beach, name='all beaches'),
    path('creat/', views.BeachCreatView.as_view(), name='creat beach'),
    # path('creat/', views.create_beaches, name='creat beach'),
    path('update/<int:pk>', views.BeachUpdateView.as_view(), name='update beach'),
    path('details/<int:pk>', views.details_beaches, name='details beach'),
    path('delete/<int:pk>', views.delete_beaches, name='delete beach'),
]