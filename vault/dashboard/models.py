from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, MinLengthValidator

# model for vault entites
class Cluster(models.Model):
    cluster_name = models.CharField(validators=[RegexValidator(r'^[a-zA-Z0-9_-]*$', 'Cluster name must not contain spaces or special characters.'), MinLengthValidator(3)], max_length=64, blank=True, null=True, unique=True, error_messages={'unique': 'cluster already exists.'})
    entities_count = models.IntegerField(blank=True, null=True)
    entities_metadata = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return str(self.cluster_name)


class Node(models.Model):
    url = models.URLField(blank=True, null=True, unique=True)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cluster)


class Alert(models.Model):
    threshold = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999999)], blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cluster)
