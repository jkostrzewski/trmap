from models import *
import json
from mongoengine import *
from django.http import HttpResponse
from helpers.isocountry import IsoCountries
import math

i = IsoCountries.IsoCountry()

def world_data(request, category):
	if category in ['', ' ']:
		category = False
	peers = GeoPeer.calculate_world_data(category=category)
	peers = GeoPeer.get_world_data()
	
	r = peers
	r = prepare_world(peers)
	

	response = HttpResponse(json.dumps(r))
	response['Access-Control-Allow-Origin'] = "*"

	return response

def nation_data(request, code):
	code = i.convert_lett(code)
	response = HttpResponse(json.dumps(GeoPeer.calculate_nation_data(code)))
	response['Access-Control-Allow-Origin'] = "*"
	return response

def prepare_world(data):
	r = {}
	m = max(data.values())
	for k, v in data.iteritems():
		r[i.convert_lett(k)] = {'fillKey':str(int(math.ceil(round((float(v)/m*10), 1)))), 'tn':v}
	return r

def most_popular_torrent(request):
	r = GeoPeer.calculate_most_popular_torrent()
	response = HttpResponse(json.dumps(r))
	response['Access-Control-Allow-Origin'] = "*"
	return response		

   