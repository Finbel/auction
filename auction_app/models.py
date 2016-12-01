from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	std = models.FloatField()
	daily_posted = models.FloatField()
	demand = models.FloatField()
	current_price = models.FloatField()
	current_quantity = models.IntegerField()