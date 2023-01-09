from django.shortcuts import render
from .forms import ClusterForm
from .models import Cluster, Node, Job
from django.db import transaction

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
        nodes_data = request.POST.get('data')
        if form.is_valid():
            form.save()
            last_cluster = Cluster.objects.last()
            urls = ["https://foo.bar", "https://foo2.bar", "https://foo3.bar"]
            print(nodes_data)
            # Create a list of Node objects
            nodes = [Node(cluster=last_cluster, node_url=url) for url in urls]
            # Use the `bulk_create` method to create all of the nodes in a single database query
            with transaction.atomic():
                Node.objects.bulk_create(nodes)
            # testing = {"employee": {"name": "sonoo", "salary": 56000, "married": "yes"}}

            '''
            /**
            *! SISTEMARE
            clusters = Cluster.objects.all()
            */
            '''
            return render(request, 'clusters.html', context={'success': 'Cluster salvato con successo', 'clusters_number': clusters_number, 'clusters_data': clusters_data})
        else:
            return render(request, 'clusters.html', context={'form': ClusterForm(), 'error': form.errors, 'clusters_number': clusters_number, 'clusters_data': clusters_data})

    return render(request, 'clusters.html', context={'form': ClusterForm(), 'clusters_number': clusters_number, 'clusters_data': clusters_data})


def alerts(request):
    return render(request, 'alerts.html')