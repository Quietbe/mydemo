from django.urls import path
from ai import views

urlpatterns = [

    path('', views.LoginView.as_view()),
    path('ai/login/', views.LoginView.as_view()),
    path('ai/get/', views.GetView.as_view()),
    path('ai/index/', views.IndexView.as_view(), name='index'),
    path('ai/logout/', views.LogoutView.as_view(), name='logout'),


]
