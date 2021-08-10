from django.urls import path
from bulgaria_trips.beaches import views

urlpatterns = [
    path('', views.all_beach, name='all beaches'),
    path('creat/', views.create_beaches, name='creat beach'),
    path('update/<int:pk>', views.update_beaches, name='update beach'),
    path('details/<int:pk>', views.details_beaches, name='details beach'),
    path('delete/<int:pk>', views.delete_beaches, name='delete beach'),
]