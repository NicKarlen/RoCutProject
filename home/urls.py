from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
  path('',views.index, name='entry'),
  path('index',views.index, name='index'),
  path('waiting_list',views.waiting_list, name='waiting_list'),
  path('about',views.about, name='about'),
  path('add_waitlist', views.add_waitlist, name='add_waitlist'),
]