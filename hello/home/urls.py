
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('options',views.options,name='options'),
    path('contact',views.contact_view,name='contact'),
]
