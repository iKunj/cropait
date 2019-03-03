from django.db import models

#All the listing of the crop produced by the farmer is saved here in this table
class farmer_crops(models.Model):
    farmer_name = models.CharField(max_length=90)
    crop_name = models.CharField(max_length=90)
    amount = models.IntegerField()
    quantity = models.IntegerField()
    bought = models.CharField(max_length=90)
    flag = models.IntegerField(default = 0)

#All the listing of the Demand by the buyer is saved here in this table
class buyer_demand(models.Model):
    buyer_name = models.CharField(max_length=90)
    crop_name = models.CharField(max_length=90)
    amount = models.IntegerField()
    quantity = models.IntegerField()
    bought = models.CharField(max_length=90)
    flag = models.IntegerField(default = 0)
    deadline = models.CharField(max_length=10)