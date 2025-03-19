from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('expeditedshipment/', views.expeditedshipment, name='expeditedshipment'),
    path('AIRCHARTERSERVICES/', views.AIRCHARTERSERVICES, name='AIRCHARTERSERVICES'),
    path('PMANAGEMENT/', views.PMANAGEMENT, name='PMANAGEMENT'),
    path('agents/', views.agents, name='agents'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('contact/', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('services_details/', views.services_details, name='services_details'),
    path('track/', views.track, name='track'),
]