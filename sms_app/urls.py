from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.func,name='func'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('search/',views.search,name='search'),

    path('Road Cycle/',views.rocyc,name='Road Cycle'),
    path('MTB cycle/',views.mtcyc,name='MTB cycle'),
    path('Foldable cycle/',views.focyc,name='Foldable cycle'),

    path('Road Cycle/home',views.home,name='home'),
    path('MTB cycle/home',views.home,name='home'),
    path('Foldable cycle/home',views.home,name='home'),
]

