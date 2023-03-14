from django.urls import path

from . import views

urlpatterns = [
    path('<int:id_pitch>/', views.index, name='index'),
]
