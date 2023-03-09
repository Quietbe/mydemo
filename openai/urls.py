from django.urls import path
from openai import views

urlpatterns = [

    path('openai/login/', views.LoginView.as_view()),
    path('openai/get/', views.GetView.as_view()),
    path('openai/index/', views.IndexView.as_view(), name='index'),

]