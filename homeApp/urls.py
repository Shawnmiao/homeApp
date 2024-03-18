from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hire_staff/', views.hire_staff, name='hire_staff'),
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/update/<str:pk>/', views.update_staff, name='update_staff'),
]
