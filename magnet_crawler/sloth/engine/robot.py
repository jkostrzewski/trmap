import time
import threading
from http_client import *
#from forum_slang_processor import process_response
from torrent_processor import process_response



class Robot(threading.Thread):
	id =False
	pool = False
	visited = {}
	end_search = False
	data_patterns = []
	session = False
	def __init__(self, pool, patterns, id=0):
		threading.Thread.__init__(self)
		self.pool = pool
		self.patterns = patterns
		end_search = False
		self.id = id
		
		#self.db_initialize()
		
	
	def check_sleep(self):
		if self.pool == [] or not self.pool:
			print 'waiting...'
			time.sleep(1);
			return True
		return False
	
	
	def run(self):
		try:
			while not self.end_search:
				if self.check_sleep():
					continue
				page = self.pool.get_page()
				if page is False:
					continue

				page_response=get_page(page.url)
				if not page_response:
					continue
				#print page.url, page.depth
				data, anchors = process_response(self, page, page_response)
				if data:
					self.pool.db.insert_geo_peer(page.args['category'], data, page.url)
				else:
					self.pool.add_pages(page, anchors)
		except KeyboardInterrupt:
			self.kill()
			print '{0} robot ended'.format(self.id)
			exit()


	def check_if_visited(self, page):
		del self.pool[0]
		if page.url in self.visited:
				return True
		else:
			self.visited[page.url] = True
	
	def kill(self):
		self.end_search = True
			
		