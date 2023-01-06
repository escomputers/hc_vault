from django.shortcuts import render
from .forms import ClusterForm
from .models import Cluster, Job
import json

def home(request):
    try:
        clusters = Cluster.objects.all()
    except Cluster.DoesNotExist:
        clusters = None

    return render(request, 'home.html', context={'clusters': clusters})


def clusters(request):
    try:
        clusters = Cluster.objects.all()
        clusters_number = len(clusters)
    except Cluster.DoesNotExist:
        clusters = None

    if request.method == 'POST':
        form = ClusterForm(request.POST)
        nodes = request.POST.get('data')
        print(nodes)
        if form.is_valid():
            form.save()
            clusters = Cluster.objects.all()
            return render(request, 'clusters.html', context={'form': ClusterForm(), 'clusters': clusters, 'success': 'Cluster salvato con successo', 'clusters_number': clusters_number})
        else:
            return render(request, 'clusters.html', context={'form': ClusterForm(), 'clusters': clusters, 'error': form.errors, 'clusters_number': clusters_number})

    return render(request, 'clusters.html', context={'form': ClusterForm(), 'clusters': clusters, 'clusters_number': clusters_number})


def alerts(request):
    return render(request, 'alerts.html')