from sloth.engine.db_manager import *
import sys


dbm = False

def main(arg):
	global dbm
	dbm = DbManager()
	
	get_geo_rank(arg)
	#get_by_nation(arg)

def get_geo_rank(category):
	cursor = dbm.db.geo_peers.find({'category':category})
	result = {}
	for c in cursor:
		data = c['data']
		
		for k, v in data.iteritems():
			if k not in result:
				result[k] = 0
			result[k]+=v

	result = sorted(result.items(), key=lambda x: x[1], reverse=False)
	for k, v in result:
		print k, v

def get_by_nation(nation):
	result = {}
	cursor = dbm.db.geo_peers.find({'data.{}'.format(nation): {'$exists':'true'}})
	for c in cursor:
		if c['category'] not in result:
			result[c['category']] = 0
		else:
			result[c['category']] += c['data'].get(nation)
	result = sorted(result.items(), key=lambda x: x[1], reverse=False)
	for k, v in result:
		print k, v





if __name__ == '__main__':
	main(sys.argv[1])