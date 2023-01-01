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

    if request.method == "POST":
        form = ClusterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'clusters.html', context={'form': ClusterForm(), 'clusters': clusters, 'success': 'Cluster salvato con successo'})
        else:
            return render(request, 'clusters.html', context={'form': ClusterForm(), 'clusters': clusters, 'error': form.errors})

    return render(request, 'clusters.html', context={'form': ClusterForm(), 'clusters': clusters})


def alerts(request):
    return render(request, 'alerts.html')