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
    # path('reads/',views.readstudent, name='read_student'),
     path('delete/', views.delete, name='delete_student'),
    path('read/', views.read_student, name='read_student'),
]
