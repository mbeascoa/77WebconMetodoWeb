from django.urls import path

from cargos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empleados', views.empleados, name='empleados'),
