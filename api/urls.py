from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.apiOverview,name="apiOverview"),
    path('list/',views.ShowAll,name="list"),
    path('show/',views.userData,name="show"),
]
