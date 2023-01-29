from .models import Cluster, Node, Alert
from django.forms import ModelForm, formset_factory, TextInput, URLInput, Select, EmailInput
from django import forms

class ClusterForm(ModelForm):
    cluster_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    class Meta:
        model = Cluster
        fields = ['cluster_name']
# use the formset factory to create the formset class
ClusterFormSet = formset_factory(ClusterForm, extra=1)

class NodeForm(ModelForm):
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'required': 'required'}), error_messages={'invalid': 'is not a valid URL'})
    # cluster = forms.ModelChoiceField(queryset=Cluster.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}),  empty_label="Select a cluster")
    class Meta:
        model = Node
        fields = ['url']
NodeFormSet = formset_factory(NodeForm, extra=1)

class AlertForm(ModelForm):
    class Meta:
        model = Alert
        fields = '__all__'

class EmailForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}))
    class Meta:
        model = Alert
        fields = ['email']
EmailFormSet = formset_factory(EmailForm, extra=1)
