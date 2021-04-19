from os import name, pardir
from django.urls import path
from task import views


urlpatterns = [
    path('', views.TaskView.as_view(), name='task'),
    path('project/', views.ProjectView.as_view(), name='project'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.login_view, name='login')
]