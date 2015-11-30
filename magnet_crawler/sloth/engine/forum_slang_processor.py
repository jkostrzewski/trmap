from http_client import *
import db_manager
from BeautifulSoup import BeautifulSoup
import re
from page import Page

#kafeteria
#search_comp = 'div'
#search_class = 'topic__content'
#output='C:\cygwin64\home\Kuba\working_dir\elektroda.txt'
#href_prefix=''

#elektroda
search_comp = 'span'
search_class = 'postbody post-message'
output='C:\cygwin64\home\Kuba\working_dir\elektroda.txt'
href_prefix='/'

def process_response(robot, page, page_response):
		pages = []
		text = ''
		content = BeautifulSoup(page_response.content).findAll(search_comp, attrs={'class': search_class})
		if content is not None:
			for item in content:
				text+=item.text
		anchors = BeautifulSoup(page_response.text).findAll('a')
		for anchor in anchors[:40]:
					if  anchor.has_key('href'):
						href = anchor['href']
						if is_same_host(page.url, href_prefix+href) is True:
							pages.append(Page(href_prefix+href, page.depth, {'action':'default'}))
		file = open(output, 'a+')
		file.writelines(text)
		file.close()
		
				
		return [], pages