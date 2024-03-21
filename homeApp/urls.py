from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hire_staff/', views.hire_staff, name='hire_staff'),
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/update/<str:pk>/', views.update_staff, name='update_staff'),
    path('new_branch/', views.branch_new, name='branch_new'),
    path('branches/', views.branch_list, name='branch_list'),
    path('branches/edit/<str:pk>/', views.branch_edit, name='branch_edit'),
]
