from django.db import models

# model for vault entites
class Node(models.Model):
    vault_node = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.vault_cluster)

class ClusterCounter(models.Model):
    counter = models.IntegerField(blank=True, null=True)
    vault_node = models.ForeignKey('Node', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.counter)
