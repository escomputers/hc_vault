from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="dashboard"),
    path("add-clusters/", views.addClusters, name="add-clusters"),
    path("add-nodes/", views.addNodes, name="add-nodes"),
    path("add-alerts/", views.addAlerts, name="add-alerts")
]
