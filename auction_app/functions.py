import csv 
import operator
import codecs
from urllib.request import urlopen

def format_date(date_string):
	YYYY = date_string[6:10]
	MM = date_string[0:2]
	DD = date_string[3:5]
	HH = date_string[11:13]
	mm = date_string[14:16]
	ss = date_string[17:19]
	new_date = YYYY+'-'+MM+'-'+DD+' '+HH+':'+mm+':'+ss
	return new_date
def demand_to_buy_koefficient(demand):
	k = -1.8
	m = 1.72
	return (demand*k+m)

def demand_to_sell_koefficient(demand):
	k = (0.6/0.4)
	m = -0.5*k
	return (demand*k+m)

def get_data():
	url = 'http://www.wowuction.com/eu/darkmoon-faire/horde/Tools/RealmDataExportGetFileStatic?type=csv&token=aD2j4zCuLSm7p3JfrbAv8A2'
	response = urlopen(url)
	# with open('auction-data.csv', newline='') as csvfile:

	# file to write to
	buy = open('buy', 'w')
	sell = open('sell','w')

	reader = csv.DictReader(codecs.iterdecode(response, 'utf-8'), delimiter=',', quotechar='|')
	sortedlist = sorted(reader, key=lambda x: float(operator.itemgetter('14-day Todays PMktPrice')(x)), reverse=True)
	return sortedlist