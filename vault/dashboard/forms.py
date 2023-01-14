from django import forms
from .models import Cluster, Node
from django.forms import ModelForm

class ClusterForm(ModelForm):
	class Meta:
		model = Cluster
		fields = ['cluster_name']

'''
class NodesForm(ModelForm):
	class Meta:
		model = Node
		fields = ['node_url']
'''
