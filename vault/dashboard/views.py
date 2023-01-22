from django.shortcuts import render
from .models import Cluster, Node, Job
from .forms import ClusterForm, NodeForm


def home(request):
    try:
        clusters = Cluster.objects.all()
        clusters_number = len(clusters)
        clusters_data = clusters.values()
        nodes = Node.objects.all()
        empty_clusters = []
        for i in clusters_data:
            clusters_ids = i.get('id')
            cluster_nodes = Node.objects.filter(cluster=clusters_ids)
            if not cluster_nodes.exists():
                empty_clusters.append(i.get('cluster_name'))
    except Cluster.DoesNotExist:
        clusters = None
        clusters_number = 0
        clusters_data = None
        nodes = None
        empty_clusters = None

    return render(request, 'home.html', context={'clusters_number': clusters_number, 'clusters_data': clusters_data, 'empty_clusters': empty_clusters, 'nodes': nodes})


def addClusters(request):
    # save data on successful submission
    if request.method == 'POST':
        cluster_form = ClusterForm(request.POST)
        if cluster_form.is_valid():
            cluster_form.save()
            return render(request, 'add-clusters.html', context={'success': 'success'})
        else:
            return render(request, 'add-clusters.html', context={'form': cluster_form})

    # GET case
    return render(request, 'add-clusters.html')


def addNodes(request):
    try:
        clusters = Cluster.objects.all()
        clusters_data = clusters.values()
        empty_clusters = []
        for i in clusters_data:
            clusters_ids = i.get('id')
            cluster_nodes = Node.objects.filter(cluster=clusters_ids)
            if not cluster_nodes.exists():
                empty_clusters.append(i.get('cluster_name'))
    except Cluster.DoesNotExist:
        clusters = None
        clusters_data = None
        empty_clusters = None

    node_form = NodeForm(request.POST or None)
    if request.method == "POST":
        if node_form.is_valid():
            node_form.save()
            return render(request, 'add-nodes.html', context={'form': node_form, 'success': 'success', 'clusters': clusters})
        else:
            return render(request, 'add-nodes.html', context={'form': node_form, 'clusters': clusters})

    return render(request, 'add-nodes.html', context={'form': node_form, 'clusters': clusters, 'empty_clusters': empty_clusters,})


def alerts(request):
    return render(request, 'alerts.html')