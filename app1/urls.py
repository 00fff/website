from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hobbies/", views.hobbies, name="hobbies"),
    
    path('hobbies/<int:hobby_id>/', views.hobby, name='hobby')
]