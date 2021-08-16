from django.contrib import admin
from django.urls import path
from csvs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.simple_upload),
]

