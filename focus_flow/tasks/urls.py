from django.urls import path, include
from django.http import HttpResponse
from . import views
app_name = 'tasks'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:tasks_id>/delete/', views.delete, name="delete"),
    path('<int:tasks_id>/update/', views.update, name="update"),
    path('add/', views.add, name="add"),
    path('toggle_complete/<int:tasks_id>/', views.toggle_complete, name='toggle_complete'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]