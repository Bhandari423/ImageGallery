from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ShowImage, name='gallery'),
    path('specificimage/<int:id>/', views.Detail),
    path('forms', views.FormView),
]