from django import forms
from .models import Cluster, ClusterNodes, Job

class ClusterForm(ModelForm):
	class Meta:
		model = Cluster
		fields = '__all__'