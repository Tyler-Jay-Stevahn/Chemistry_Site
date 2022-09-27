from django.urls import path

from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('home/new/', second_page, name='new'),
    path('contact/', contact, name='contact'),
    path('date/<int:year>/', datepage, name='datepage'),
    path('signup/', signuppage, name='signuppage'),
    path('adduser/', adduser, name='adduser'),
    path('', landingpage, name='landingpage')
]