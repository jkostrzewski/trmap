from pymongo import MongoClient
import datetime

class DbManager:

	db_client = False
	db = False

	def __init__(self):
		self.db_client = MongoClient('localhost', 27017)
		self.db = self.db_client.torrent_map_db


	def insert_geo_peer(self, category, geo_peer_map, link):
		data ={
			'category' : category,
			'timestamp' : datetime.datetime.now(),
			'data': geo_peer_map,
			'link' : link
		}
		return self.db.geo_peers.insert_one(data).inserted_id