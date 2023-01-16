from django import forms
from .models import Cluster, Job
from django.forms import ModelForm

class ClusterForm(ModelForm):
	class Meta:
		model = Cluster
		fields = '__all__'
