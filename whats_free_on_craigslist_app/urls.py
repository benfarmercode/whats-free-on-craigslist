from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('listings', views.ListingView.as_view(), name='listings')
]
