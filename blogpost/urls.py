from django.urls import path
from .views import home, post_create, post_view, search

urlpatterns = [
    path('', home, name='home'),
    path('post/create/', post_create, name='post_create'),
    path('post/view/<slug:slug>/', post_view, name='post_view'),
    path('search/', search, name='search'),
]