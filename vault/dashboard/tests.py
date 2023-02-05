from django.test import RequestFactory, TestCase
from .models import Cluster, Node, Alert
from .views import addClusters, addNodes
from django.test import Client

class HomeViewTest(TestCase):
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
        # Create a request simulating a client request
        client = Client()

        response = client.get('')

        # Check that the response has a status code of 200
        self.assertEqual(response.status_code, 200)

        # Check that the correct context variables are passed to the template
        self.assertEqual(len(response.context['clusters_data']), 2)
        self.assertEqual(len(response.context['empty_clusters']), 0)
        self.assertEqual(len(response.context['cluster_urls']), 2)
        self.assertEqual(response.context['clusters_number'], 2)


class AddClustersViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_add_clusters_view_post_request(self):
        # Simulate a successful POST request to the view
        request = self.factory.post('/add-clusters/', data={
            'form-TOTAL_FORMS': '3', 'form-INITIAL_FORMS': '0', 
            'form-0-cluster_name': 'cluster_1', 
            'form-1-cluster_name': 'cluster_2', 
            'form-2-cluster_name': 'cluster_3'
        })

        response = addClusters(request)

        # Check if the response has a status code of 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if clusters were added
        self.assertEqual(Cluster.objects.count(), 3)

        # Check if the response contains the success message
        self.assertContains(response, 'success')

    def test_add_clusters_view_get_request(self):
        # Simulate a GET request to the view
        request = self.factory.get('/add-clusters/')
        response = addClusters(request)

        # Check if the response has a status code of 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the formset in the context
        self.assertContains(response, 'formset')


class AddNodesTest(TestCase):
    def setUp(self):
        # create some clusters
        self.cluster1 = Cluster.objects.create(cluster_name='Cluster1')
        self.cluster2 = Cluster.objects.create(cluster_name='Cluster 2')
        
        # request factory
        self.factory = RequestFactory()

    def test_add_nodes_view_post_request(self):
        # send a post request with valid form data
        request = self.factory.post('/add-nodes/', data={
            'cluster': self.cluster1.id,
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 0,
            'form-0-url': 'https://test04.com',
            'form-1-url': 'https://test05.com',
        })

        response = addNodes(request)

        # Check if the response was successful and the nodes were added
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Node.objects.count(), 2)
        self.assertContains(response, 'success')


    def test_add_nodes_view_get_request(self):
        # Simulate a GET request to the view
        request = self.factory.get('/add-nodes/')
        response = addNodes(request)

        # Check if the response has a status code of 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the formset in the context
        self.assertContains(response, 'formset')