from django.urls import path

from . import views

app_name = "orders"
urlpatterns = [
    path('<int:id_pitch>/', views.index, name='orders'),
    path('<int:id_pitch>/place_order',views.place_order,name="place_order")
]
