from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='website-index'),
    path('contact/', views.contact, name='website-contact'),
    path('signup/', views.signUp, name='signup'),
]