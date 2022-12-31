from django import forms
from django.forms import ModelForm
from .models import Cluster, Job

class ClusterForm(ModelForm):
	class Meta:
		model = Cluster
		fields = '__all__'