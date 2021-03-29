from django.db import models

class Dealer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    dealer_id = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
