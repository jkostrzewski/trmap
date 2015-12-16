from mongoengine import *
from mongoengine.queryset import queryset_manager
from model_helper import *
from django.core.cache import cache
import re


class GeoPeerData(EmbeddedDocument):
    code = StringField()
    count = StringField()

class GeoPeer(Document):
    category = StringField()
    link = StringField()
    timestamp = DateTimeField()
    data = ListField(EmbeddedDocumentField(GeoPeerData))

    meta = {
    	'collection': 'geo_peers',
    	'ordering':'-timestamp'
    }

    @staticmethod
    def calculate_world_data2(date=False, number=False, category=False, keyword=False, collection=False):
    	if collection:
    		coll = collection
    	else:
    		coll = world_data_default_coll
    	geo_peers = GeoPeer.objects()
    	if category:
    		geo_peers = geo_peers.filter(category=category)
    	if number:
    		if geo_peers.count()>number:
    			geo_peers = geo_peers[:number]
    	if keyword:
    		geo_peers = geo_peers.filter(link__contains=keyword)
    	geo_peers = geo_peers.order_by('category', 'link')
    	result = geo_peers.map_reduce(world_data_mapper, world_data_reducer, {'replace':'out'}, limit=1)
    	result = {r.key:r.value for r in result}
    	return result

    @staticmethod
    def calculate_world_data(date=False, number=False, category=False, keyword=False, collection=False):
    	geo_peers_col = GeoPeer._get_collection()
    	query = {'link': re.compile(r'Fallout')}
    	result = geo_peers_col.inline_map_reduce(world_data_mapper, world_data_reducer, sort={'timestamp':-1}, query=query)
    	result = {r['_id']:r['value'] for r in result}
    	cache.set('world_data', result, timeout=999999)
    	return result



    @staticmethod
    def get_world_data():
    	data = cache.get('world_data')
    	if not data:
    		GeoPeer.calculate_world_data()
    	return cache.get('world_data')


    @staticmethod
    def calculate_nation_data(code, collection=False):
    	if collection:
    		coll = collection
    	else:
    		coll = nation_default_coll
    	geo_peers = GeoPeer.objects
    	result = geo_peers.map_reduce(nation_data_mapper(code), nation_data_reducer, 'inline', limit=500)
    	return {x.key: x.value for x in result}

    @staticmethod
    def calculate_most_popular_torrent():
    	geo_peers_col = GeoPeer._get_collection()
    	result = geo_peers_col.inline_map_reduce(most_pop_torr_mapper, most_pop_torr_reducer, sort={'timestamp':-1}, limit=100)
    	print len(result)
    	return sorted(result, key=lambda x:x.items()[1], reverse=True)
