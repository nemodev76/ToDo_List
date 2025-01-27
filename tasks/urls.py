from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('check/<int:id>/', views.check_task, name='check_task'),
    path('uncheck/<int:id>/', views.uncheck_task, name='uncheck_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
]