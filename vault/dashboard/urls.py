from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="dashboard"),
    path("get-cluster/", views.getCluster, name="get-cluster"),
    path("submit/", views.submit, name="submit"),
    path("clusters/", views.clusters, name="clusters"),
    path("alerts/", views.alerts, name="alerts")
]
