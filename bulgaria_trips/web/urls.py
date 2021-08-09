from django.urls import path
from bulgaria_trips.web.views import IndexView, FactsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('facts/', FactsView.as_view(), name='facts'),
]
