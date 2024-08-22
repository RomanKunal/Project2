from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('submit/', views.create),
    path('read/', views.read),
    path('read_students/', views.read_student),
    path('update/', views.update, name='update'),
]
