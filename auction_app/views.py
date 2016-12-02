from django.shortcuts import render
from django.db.models import F, Q
from .functions import get_data, demand_to_buy_koefficient, demand_to_sell_koefficient, format_date
from .models import Item, Time
import csv 

# Create your views here.
def front(request):
	time = Time.objects.all().first()
	return render(request, 'auction_app/front.html', {'time' : time})

def buy(request):
	items = Item.objects.filter(current_price__lte=F('buy_for'), current_quantity__gte=1)
	return render(request, 'auction_app/buy.html', {'items': items})

def sell(request):
	items = Item.objects.filter(Q(current_price__gte=F('sell_for')) | Q(current_quantity=0))
	return render(request, 'auction_app/sell.html', {'items': items})

def update(request):
	print("We get data!")
	data = get_data()
	time,created = Time.objects.get_or_create(
				time_id = 1
			)
	time.updated = format_date(data[1]['Export Time'])
	time.save()
	for row in data:
		data_item_id = int(row['Item ID'])
		data_name = row['Item Name']
		data_price = float(row['14-day Median Market Price'])
		data_std = float(row['Median Market Price StdDev'])
		data_daily_posted = float(row['Avg Daily Posted'])
		data_demand = float(row['Estimated Demand'])
		data_current_price = float(row['AH MinimumPrice'])
		data_current_quantity = float(row['AH Quantity'])

		std_area = (data_price*0.9) > data_std and data_std > (data_price*0.2)
		price_area = 100 > data_price and data_price > 2
		posted_area = data_daily_posted > 50
		demand_area = data_demand > 0.2

		if std_area and price_area and demand_area and posted_area:
			item, created = Item.objects.get_or_create(
				item_id = data_item_id,
				name = data_name,
			)

			data_buy_for = data_price-data_std*demand_to_buy_koefficient(data_demand)
			data_sell_for = data_price+data_std*demand_to_sell_koefficient(data_demand)

			item.price = data_price
			item.std = data_std
			item.daily_posted = data_daily_posted
			item.demand = data_demand
			item.current_price = data_current_price
			item.current_quantity = data_current_quantity
			item.buy_for = data_buy_for
			item.sell_for = data_sell_for
			item.save()
		else :
			Item.objects.filter(item_id=data_item_id).delete()
	return render(request, 'auction_app/update.html', {})