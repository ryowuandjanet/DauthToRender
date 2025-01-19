from django.urls import path
from . import views

urlpatterns = [
    path('', views.yfcase_list, name='yfcase_list'),
    path('create/', views.yfcase_create, name='yfcase_create'),
    path('<int:id>/detail/', views.yfcase_detail, name='yfcase_detail'),
    path('<int:id>/update/', views.yfcase_update, name='yfcase_update'),
    path('<int:id>/delete/', views.yfcase_delete, name='yfcase_delete'),
]