from django.shortcuts import render
from .models import Cluster, Node, Job
from django.db import transaction
import json

def home(request):
    try:
        clusters = Cluster.objects.all()
    except Cluster.DoesNotExist:
        clusters = None

    return render(request, 'home.html', context={'clusters': clusters})


def clusters(request):
    if request.method == 'POST':
        data_str = request.POST.get('data')
        data_dict = json.loads(data_str)
        cluster_name = data_dict.get('0')
        try:
            cluster = Cluster.objects.get(cluster_name=cluster_name)
        except Cluster.DoesNotExist:
            cluster = Cluster.objects.create(cluster_name=cluster_name)
            last_cluster = Cluster.objects.last()
            urls = data_dict.get('1')
            # Create a list of Node objects
            nodes = [Node(cluster=last_cluster, node_url=url) for url in urls]
            # Use the `bulk_create` method to create all of the nodes in a single database query
            with transaction.atomic():
                Node.objects.bulk_create(nodes)
        finally:
            return render(request, 'clusters.html')
        '''
        /**
        *! SISTEMARE
        clusters = Cluster.objects.all()
        */
        '''
        '''
            return render(request, 'clusters.html', context={'success': 'Cluster salvato con successo', 'clusters_number': clusters_number, 'clusters_data': clusters_data})
        else:
            return render(request, 'clusters.html', context={'form': ClusterForm(), 'error': form.errors, 'clusters_number': clusters_number, 'clusters_data': clusters_data})
        '''
    else:
        try:
            clusters = Cluster.objects.all()
            clusters_number = len(clusters)
            clusters_data = clusters.values()
        except Cluster.DoesNotExist:
            clusters = None
        finally:
            return render(request, 'clusters.html', context={'clusters_number': clusters_number, 'clusters_data': clusters_data})


def alerts(request):
    return render(request, 'alerts.html')