from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="dashboard"),
    path("clusters/", views.clusters, name="clusters"),
    path("jobs/", views.jobs, name="jobs")
]
