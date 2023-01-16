from django.shortcuts import render
from .models import Cluster, Node, Job
from django.db import transaction
import json
from .forms import ClusterForm
from django.http import JsonResponse
from django.core import serializers


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


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
        clusters_number = 0
        clusters_data = None

    # save data on successful submission
    if request.method == 'POST':
        cluster_form = ClusterForm(request.POST)
        if cluster_form.is_valid():
            cluster_form.save()
            clusters = Cluster.objects.all()
            clusters_number = len(clusters)

        return render(request, 'clusters.html', context={'form': cluster_form, 'clusters_number': clusters_number, 'clusters_data': clusters_data, 'success': 'Cluster saved!'})

    # GET case
    return render(request, 'clusters.html', context={'clusters_number': clusters_number, 'clusters_data': clusters_data})


def getCluster(request):
    # request should be ajax and method should be GET
    if is_ajax(request=request) and request.method == "GET":
        # get the cluster from the client side
        cluster_name = request.GET.get("cluster_name", None)
        # check for cluster existence in the database
        if Cluster.objects.filter(cluster_name = cluster_name).exists():
            # if cluster_name found return not valid new friend
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if cluster is not found, then user can create a new cluster
            return JsonResponse({"valid":True}, status = 200)

    # error handling
    return JsonResponse({}, status = 400)


def nodes(request):
    # request should be ajax and method should be POST.
    if is_ajax(request=request) and request.method == "POST":
        data_str = request.POST.get('data')
        
        if data_str is not None:
            data_dict = json.loads(data_str)
            urls = data_dict.get('1')
            try:
                for url in urls:
                    url = Node.objects.get(node_url=url)
                    return JsonResponse({"error": "Node exists"}, status=400)
            except Node.DoesNotExist:
                last_cluster = Cluster.objects.last()
                # Create a list of Node objects
                nodes = [Node(cluster=last_cluster, node_url=url) for url in urls]
                # Use the `bulk_create` method to create all of the nodes in a single database query
                with transaction.atomic():
                    Node.objects.bulk_create(nodes)

                return JsonResponse({"success": data_str}, status=200)

    # some form errors occured
    return JsonResponse({"error": ""}, status=400)


def submit(request):
    # request should be ajax and method should be POST.
    if is_ajax(request=request) and request.method == "POST":
        # get the form data
        cluster_form = ClusterForm(request.POST)
        # save the data and after fetch the object in instance
        if cluster_form.is_valid():
            instance = cluster_form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured
            return JsonResponse({"error": cluster_form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def alerts(request):
    return render(request, 'alerts.html')