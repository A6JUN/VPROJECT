from django.urls import path
from userside import views

urlpatterns=[
    path('Buypage/',views.Buypage,name="Buypage"),
    path('Oder/<int:proid>',views.Oder,name="Oder")
]