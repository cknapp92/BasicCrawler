from lxml import html
import requests

class AppCrawler: 

	def __init__ (self, starting_url, depth):
		self.starting_url = starting_url
		self.depth = depth
		self.apps = []

	def crawl(self):
		self.get_app_from_link(self.starting_url)
		return

	def get_app_from_link(self, link):
		start_page = requests.get(link)
		tree = html.fromstring(start_page.text)

		name = tree.xpath('//div[@id="bodyWrap"]//h1[@id="productNameHeader"]/text()')
		price = tree.xpath('//div[@id="bodyWrap"]//span[@class="regPrice"]/text()')[0]


		print (name)
		print (price)

		return

class App:

	def __init__ (self, name, developer, price, links):
		self.name = name 
		self.developer = developer
		self.price = price
		self.links = links

	def __str__ (self):
		return ("Name: " + self.name.encode('UTF-8') +
		"\r\nDeveloper: " + self.developer.encode('UTF-8') +
		"\r\nPrice: " + self.price.encode('UTF-8') + "\r\n")

crawler = AppCrawler('https://www.crateandbarrel.com/stirrup-antique-bronze-table-lamp/s215483?lkhd_id=xkyYCp&lkhd_type=fallback', 0)
crawler.crawl()

for app in crawler.apps:
	print (app)