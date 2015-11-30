from lxml import etree

class IsoCountry:

	world_atlas_path = 'input/worldatlas.html'
	data = {}

	def __init__(self):
		self.parse_world_atlas()
		pass

	def parse_world_atlas(self):
		root = etree.parse(self.world_atlas_path)
		for tr in root.xpath('/table/tr'):
			full = tr.xpath("td[@class='cell01']")[0].text.strip()
			two_lett = tr.xpath("td[@class='cell02']")[0].text.strip()
			three_lett = tr.xpath("td[@class='cell03']")[0].text.strip()
			self.data[two_lett] = {}
			self.data[two_lett]['full']=full
			self.data[two_lett]['three_lett']=three_lett

	def get_full_name(self, two_lett):
		try:
			return self.data[two_lett]['full']
		except KeyError:
			return False

	def get_three_lett(self, two_lett):
		try:
			return self.data[two_lett]['three_lett']
		except KeyError:
			return False

if __name__ == '__main__':
	#test with Poland
	c = IsoCountry()
	print c.get_full_name('PL')
	print c.get_three_lett('PL')
