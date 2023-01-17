from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


# model for vault entites
class Cluster(models.Model):
    cluster_name = models.CharField(max_length=64, blank=True, null=True, unique=True)
    entities_count = models.IntegerField(blank=True, null=True)
    entities_metadata = models.CharField(max_length=256, blank=True, null=True)
    threshold = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999)], blank=True, null=True)
    json_nodes = models.JSONField(unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.cluster_name)
'''
class Node(models.Model):
    node_url = models.URLField()
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cluster_name)
'''


class Job(models.Model):
    email = models.EmailField(blank=True, null=True, unique=True)
    cc = models.EmailField(blank=True, null=True, unique=True)
    cc2 = models.EmailField(blank=True, null=True, unique=True)
    cc3 = models.EmailField(blank=True, null=True, unique=True)
    cluster_name = models.ForeignKey(Cluster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
