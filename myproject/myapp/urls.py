from django.urls import path
from django.contrib.auth import views as auth_views
from .views import filtered_questions,save_answer,questions


urlpatterns = [
    path('',filtered_questions,name='filtered_questions'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('save_answer/',save_answer,name='save_answer'),
    path('questions/',questions,name='questions')
]