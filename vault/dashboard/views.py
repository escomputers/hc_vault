from django.shortcuts import render
from .models import Cluster, Node, Alert
from .forms import ClusterFormSet, NodeFormSet, EmailFormSet, AlertForm


def home(request):
    try:
        clusters_number = len(Cluster.objects.all())
        clusters_data = Cluster.objects.all().values()
        empty_clusters = []
        cluster_urls = Node.objects.filter(cluster__isnull=False)
        for i in clusters_data:
            clusters_ids = i.get('id')
            cluster_nodes = Node.objects.filter(cluster=clusters_ids)
            if not cluster_nodes.exists():
                empty_clusters.append(i.get('cluster_name'))
    except Cluster.DoesNotExist:
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
            return render(request, 'add-clusters.html', context={'formset': ClusterFormSet(), 'success': 'success'})
        else:
            return render(request, 'add-clusters.html', context={'formset': cluster_form})

    return render(request, 'add-clusters.html', context={'formset': cluster_form})


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

    if request.method == "POST":
        cluster_id = request.POST.get('cluster')
        cluster = Cluster.objects.get(id=cluster_id)
        node_form = NodeFormSet(request.POST)
        if node_form.is_valid():
            for item in node_form:
                node = item.save(commit=False)
                node.cluster = cluster
                node.save()
            return render(request, 'add-nodes.html', context={'formset': NodeFormSet(), 'success': 'success', 'clusters': clusters})
        else:
            return render(request, 'add-nodes.html', context={'formset': node_form, 'clusters': clusters})

    return render(request, 'add-nodes.html', context={'formset': NodeFormSet(), 'clusters': clusters, 'empty_clusters': empty_clusters})


def addAlerts(request):
    try:
        clusters = Cluster.objects.all()
        # clusters_data = clusters.values()
        # empty_clusters = []
        '''
        for i in clusters_data:
            clusters_ids = i.get('id')
            cluster_nodes = Node.objects.filter(cluster=clusters_ids)
            if not cluster_nodes.exists():
                empty_clusters.append(i.get('cluster_name'))
        '''
    except Cluster.DoesNotExist:
        clusters = None
        # clusters_data = None
        # empty_clusters = None

    if request.method == "POST":
        cluster_id = request.POST.get('cluster')
        cluster = Cluster.objects.get(id=cluster_id)
        alert_form = AlertForm(request.POST)
        email_formset = EmailFormSet(request.POST)
        if alert_form.is_valid() and email_formset.is_valid():
            threshold = request.POST.get('threshold')
            for item in email_formset:
                alert = item.save(commit=False)
                alert.cluster = cluster
                alert.threshold = threshold
                alert.save()
            return render(request, 'add-alerts.html', context={'form': AlertForm(), 'formset': EmailFormSet(), 'success': 'success', 'clusters': clusters})
        else:
            return render(request, 'add-alerts.html', context={'form': alert_form, 'formset': email_formset, 'clusters': clusters})

    return render(request, 'add-alerts.html',  context={'form': AlertForm(), 'formset': EmailFormSet(), 'clusters': clusters})