from django.db import models

# Create your models here.
class Tour(models.Model):
    # we need origin country, we need destination, number of night and we need the price for the tour
    origin_country=models.CharField(max_length=64)
    destination_country=models.CharField(max_length=64)
    number_of_nights=models.IntegerField()
    price=models.IntegerField()
    def __str__(self):
        return (f"From {self.origin_country} To {self.destination_country} {self.number_of_nights} number of nights and costs is $  {self.price}")
    