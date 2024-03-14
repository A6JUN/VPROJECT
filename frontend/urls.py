from django.urls import path
from frontend import views

urlpatterns=[
 path('main/',views.main,name="main"),
 path('homepage/',views.homepage,name="homepage"),
 path('prdtdatasave/',views.prdtdatasave,name="prdtdatasave"),
 path('prdtdisplay/',views.prdtdisplay,name="prdtdisplay"),
 path('prdtdelete/<int:dataid>', views.prdtdelete, name="prdtdelete"),
 path('prdtupdate/<int:dataid>', views.prdtupdate, name="prdtupdate"),
 path('prdtedit/<int:dataid>', views.prdtedit, name="prdtedit"),


]
