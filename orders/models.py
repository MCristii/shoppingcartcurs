from django.db import models


class Order(models.Model):
    nume_produs = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('nume_produs',)
        index_together = (('id'),)

    def __str__(self):
        return self.nume_produs