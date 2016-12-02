from django.db import models

# Create your models here.
class Time(models.Model):
	time_id = models.IntegerField(default=1,primary_key=True)
	updated = models.DateTimeField(null=True)

class Item(models.Model):
	item_id = models.IntegerField(default=0,primary_key=True)
	name = models.CharField(max_length=200)
	price = models.FloatField(default=-1)
	std = models.FloatField(default=-1)
	daily_posted = models.FloatField(default=-1)
	demand = models.FloatField(default=-1)
	current_price = models.FloatField(default=-1)
	current_quantity = models.IntegerField(default=-1)
	buy_for = models.FloatField(default=-1)
	sell_for = models.FloatField(default=-1)

	def __str__(self):
		return self.name