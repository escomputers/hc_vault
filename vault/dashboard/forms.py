from django import forms
from .models import Cluster, Job

class ClusterForm(forms.ModelForm):
	class Meta:
		model = Cluster
		fields = '__all__'