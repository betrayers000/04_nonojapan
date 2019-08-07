from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('detail/<int:post_id>/', views.detail),
    path('edit/<int:post_id>/', views.edit),
    path('update/<int:post_id>/', views.update),
    path('delete/<int:post_id>/', views.delete),
]
