from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='website-index'),
    path('contact/', views.contact, name='website-contact'),
    path('signup/', views.signUp, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='website/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='website/logout.html'), name='logout'),
]