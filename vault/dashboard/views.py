from django.shortcuts import render
from .forms import ClusterForm
from .models import Cluster, Job


def home(request):
    return render(request, 'home.html')


def clusters(request):
    try:
        clusters = Cluster.objects.all()
    except Cluster.DoesNotExist:
        clusters = 'No clusters'

    form = ClusterForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'clusters.html', context={'form': ClusterForm(), 'clusters': clusters})


def jobs(request):
    return render(request, 'jobs.html')