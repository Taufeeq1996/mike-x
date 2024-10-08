from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('like/<int:post_id>/', views.like, name='like'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
]