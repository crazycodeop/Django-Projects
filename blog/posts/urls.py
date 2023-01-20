from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post')
]