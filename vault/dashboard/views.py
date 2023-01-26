from django.shortcuts import render
from .models import Cluster, Node, Job
from .forms import ClusterFormSet, NodeForm


def home(request):
    try:
        clusters = Cluster.objects.all()
        clusters_number = len(clusters)
        clusters_data = clusters.values()
        empty_clusters = []
        cluster_urls = Node.objects.filter(cluster__isnull=False)
        for i in clusters_data:
            clusters_ids = i.get('id')
            cluster_nodes = Node.objects.filter(cluster=clusters_ids)
            if not cluster_nodes.exists():
                empty_clusters.append(i.get('cluster_name'))
    except Cluster.DoesNotExist:
        clusters = None
        clusters_number = 0
        clusters_data = None
        empty_clusters = None
        cluster_urls = None

    return render(request, 'home.html', context={'clusters_number': clusters_number, 'clusters_data': clusters_data, 'empty_clusters': empty_clusters, 'cluster_urls': cluster_urls})


def addClusters(request):
    cluster_form = ClusterFormSet()
    # save data on successful submission
    if request.method == 'POST':
        cluster_form = ClusterFormSet(request.POST)
        if cluster_form.is_valid():
            for item in cluster_form:
                item.save()
            return render(request, 'add-clusters.html', context={'form': ClusterFormSet(), 'success': 'success'})
        else:
            return render(request, 'add-clusters.html', context={'form': cluster_form})

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