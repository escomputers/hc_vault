from .models import Cluster, Node, Job
from django.forms import ModelForm, formset_factory, TextInput
from django import forms

class ClusterForm(ModelForm):
    cluster_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    class Meta:
        model = Cluster
        fields = ['cluster_name']
# use the formset factory to create the formset class
ClusterFormSet = formset_factory(ClusterForm, extra=1)

class NodeForm(ModelForm):
    class Meta:
        model = Node
        fields = ['url', 'cluster']

