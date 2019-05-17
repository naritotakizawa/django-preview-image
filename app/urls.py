from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.ImageList.as_view(), name='image_list'),
    path('add/', views.ImageAdd.as_view(), name='image_add'),
    path('update/<int:pk>/', views.ImageUpdate.as_view(), name='image_update'),
]
