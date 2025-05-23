from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # ex: Cordas, Sopro, Percussão
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name