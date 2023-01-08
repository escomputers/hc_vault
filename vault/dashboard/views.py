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
        clusters_data = clusters.values()
    except Cluster.DoesNotExist:
        clusters = None

    if request.method == 'POST':
        form = ClusterForm(request.POST)
        nodes = request.POST.get('data')
        print(nodes)
        if form.is_valid():
            form.save()
            clusters = Cluster.objects.all()
            return render(request, 'clusters.html', context={'form': ClusterForm(), 'success': 'Cluster salvato con successo', 'clusters_number': clusters_number, 'clusters_data': clusters_data})
        else:
            return render(request, 'clusters.html', context={'form': ClusterForm(), 'error': form.errors, 'clusters_number': clusters_number, 'clusters_data': clusters_data})

    return render(request, 'clusters.html', context={'form': ClusterForm(), 'clusters_number': clusters_number, 'clusters_data': clusters_data})


def alerts(request):
    return render(request, 'alerts.html')