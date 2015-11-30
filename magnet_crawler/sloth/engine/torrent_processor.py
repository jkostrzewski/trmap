from http_client import *
import db_manager
from bs4 import BeautifulSoup
import re
from page import Page
from PeerManager import PeerManager
from IpUtils import *


search_comp = 'span'
search_class = 'postbody post-message'

def process_response(robot, page, page_response):
		out_urls = []
		soup = BeautifulSoup(page_response.text, 'html.parser')
		pages = []
		anchors = soup.findAll('a')
		result = False
		if 'action' not in page.args:
			for a in anchors:
				if a.has_attr('href'):
					href = a['href']
					if re.compile('^/torrent/').match(href):
						pages.append(Page(href, page.depth, {'action':'get_magnet', 'category':page.args['category']}))
		elif page.args['action'] == 'get_magnet':
			for a in anchors:
				if not a.has_attr('href'):
					continue
				href = a['href']
				if not re.match('^magnet:', href):
					continue
				magnet = get_hash_from_magnet(href)
				pm = PeerManager()
				result = {}
    			peers = pm.get_peers(magnet, iterations=7)
    			for p in peers:
        			ip = Ip(p)
        			country = ip.get_country()
        			if country:
        				if country not in result:
	        				result[country] = 1
        				else:
	        				result[country] += 1

			print page.args['category'], result
				
				
		return result, pages