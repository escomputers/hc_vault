from django import forms
from .models import Cluster, Node, Job
from django.forms import ModelForm, Select

class ClusterForm(ModelForm):
	class Meta:
		model = Cluster
		fields = ['cluster_name']

class NodeForm(ModelForm):
	class Meta:
		model = Node
		fields = ['url', 'cluster']

