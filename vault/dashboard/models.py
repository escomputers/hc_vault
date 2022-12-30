from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# model for vault entites
class Node(models.Model):
    vault_node = models.CharField(max_length=100, blank=True, null=True, unique=True)
    alert = models.BooleanField(default=False)
    threshold = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999)], blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    cc = models.EmailField(blank=True, null=True, unique=True)
    cc2 = models.EmailField(blank=True, null=True, unique=True)
    cc3 = models.EmailField(blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.vault_cluster)

class ClusterCounter(models.Model):
    counter = models.IntegerField(blank=True, null=True)
    vault_node = models.ForeignKey('Node', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.counter)
