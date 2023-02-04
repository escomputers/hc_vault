from django.shortcuts import reverse
from django.test import RequestFactory, TestCase
from .models import Cluster, Node, Alert
from .forms import ClusterFormSet, NodeFormSet, EmailFormSet, AlertForm
from .views import home, addClusters


class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a couple of clusters
        self.cluster_1 = Cluster.objects.create(cluster_name="cluster 1")
        self.cluster_2 = Cluster.objects.create(cluster_name="cluster 2")

        # Create a couple of nodes
        self.node_1 = Node.objects.create(url="url 1", cluster=self.cluster_1)
        self.node_2 = Node.objects.create(url="url 2", cluster=self.cluster_2)

        # Create a request factory
        self.factory = RequestFactory()

    def test_home_view(self):
        # Create a request
        request = self.factory.get(reverse('dashboard'))

        # Use the request to get the response from the home view
        response = home(request)

        # Check that the response has a status code of 200
        self.assertEqual(response.status_code, 200)

        # Check that the correct context variables are passed to the template
        self.assertEqual(len(response.context['clusters_data']), 2)
        self.assertEqual(len(response.context['empty_clusters']), 0)
        self.assertEqual(len(response.context['cluster_urls']), 2)
        self.assertEqual(response.context['clusters_number'], 2)

    def test_addClusters_view(self):
        # Create a request with POST data
        request = self.factory.post(reverse('add-clusters'), data={
            'cluster_set-TOTAL_FORMS': 1,
            'cluster_set-INITIAL_FORMS': 0,
            'cluster_set-MIN_NUM_FORMS': 0,
            'cluster_set-MAX_NUM_FORMS': 1000,
            'cluster_set-0-cluster_name': 'cluster 3',
        })

        # Use the request to get the response from the addClusters view
        response = addClusters(request)

        # Check that the response has a status code of 200
        self.assertEqual(response.status_code, 200)

        # Check that the cluster was created
        self.assertEqual(Cluster.objects.count(), 3)
        self.assertEqual(Cluster.objects.get(cluster_name="cluster 3").cluster_name, "cluster 3")

        # Check that the form was passed to the template
        self.assertIsInstance(response.context['formset'], ClusterFormSet)