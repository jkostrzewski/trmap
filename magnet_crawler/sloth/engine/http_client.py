import requests
import re
from urlparse import *

def get_page(page):
	try:
		response = requests.get(page, timeout=10, allow_redirects=True)		
		response.encoding = 'utf-8'
		return response
	except Exception as exc:
		print page.encode('utf-8'), 'caused an exception' + str(exc)
		return False
		
def get_text(response):
	return response.text
	
def get_hostname(root_page):
	parsed =  urlparse(root_page)
	result = str(parsed.scheme)+"://"+str(parsed.hostname)
	return result

def is_same_host(base_url, new_url):
	if new_url.startswith('/'):
		return True
	if re.compile('[\w]+\.[\w#\?]+').match(new_url):
		return True
	if get_hostname(base_url) == get_hostname(new_url):
		return True
	return False
		
def get_anchors(page):
	hrefs = re.findall('href="(https?://[\w\./?=+&-^ ]+[^.png^.pdf^.jpg^.css])"', page)
	relatives = re.findall('href="(/.+^ )"', page)
	return hrefs+relatives
	
	

def normalize_url(hostname, url):
	if url.startswith('/'):
		return hostname+url
	else:
		return url
	
if __name__ == '__main__':
	main()