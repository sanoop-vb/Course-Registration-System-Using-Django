from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('register/<int:course_id>/', views.course_register, name='course_register'),
]
