from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('pred', views.pred, name='pred'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
   ]
