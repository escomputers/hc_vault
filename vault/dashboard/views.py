from django.shortcuts import render
from .forms import ClusterForm
from .models import Cluster, Job


def home(request):
    try:
        clusters = Cluster.objects.all()
    except Cluster.DoesNotExist:
        clusters = None

    return render(request, 'home.html', context={'clusters': clusters})


def clusters(request):
    try:
        clusters = Cluster.objects.all()
    except Cluster.DoesNotExist:
        clusters = None

    form = ClusterForm(request.POST or None)
    if request.method == "POST":	
        if form.is_valid():
            form.save()
    return render(request, 'clusters.html', context={'form': ClusterForm(), 'clusters': clusters})


def jobs(request):
    return render(request, 'jobs.html')