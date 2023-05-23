# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<str:pk>/', views.view_post, name='view_post'),
    path('post/<str:pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<str:pk>/delete/', views.delete_post, name='delete_post'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
