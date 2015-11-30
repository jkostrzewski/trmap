import logging
import time
from btdht import DHT
import random

class PeerManager:

	def __init__(self):
		pass

	def get_peers(self, magnet, iterations=5):
		dht = DHT(host='0.0.0.0', port=0)
		dht.start()
	   	dht.bootstrap('router.bittorrent.com', 6881)
		dht.ht.add_hash(magnet.decode("hex"))
		result = []
		for count in xrange(iterations):
			peers = dht.ht.get_hash_peers(magnet.decode("hex"))
			for peer in peers:
				result.append((peer))
			time.sleep(3)
		dht.stop()
		return [p[0] for p in list(set(result))]

    	
