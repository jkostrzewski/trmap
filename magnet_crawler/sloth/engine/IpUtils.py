from geoip import geolite2 as g
import re

class Ip:
	NOT_FOUND = 'NA'
	def __init__(self, string_ip):
		self.string_ip = string_ip

	def get_country(self):
		match = g.lookup(self.string_ip)
		if match:
			return match.country
		else:
			return self.NOT_FOUND

def get_hash_from_magnet(magnet):	
	h = re.search('btih:(.*)\&dn', magnet).group(1)
	return h