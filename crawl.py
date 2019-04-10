import requests
from bs4 import BeautifulSoup as bs


class Crawler():

	def __init__(self):
		'''
		Init the parameters for crawling
		'''

		self.url = "https://www.pcstore.com.tw/adm/psearch.htm"
		self.payload = {'ltg_p':'', 'after_login':'', 'slt_k_option':1, 'store_k_word':''}
		self.encoding = 'Big5'
		self.keyword = ''
		self.page = ''

	def Idle(self):
		'''
		for user input
		'''

		self.keyword = input('請輸入想查詢關鍵字: ')

	def GetPage(self):
		'''
		get search page
		'''
		self.payload['store_k_word'] = self.keyword.encode('Big5')
		res = requests.post(self.url, data=self.payload)
		res.encoding = 'Big5'

		self.page = res.text


	def ParseAndReturnResult(self):
		'''
		Get results
		'''
		soup = bs(self.page, 'html.parser')
		title_list = soup.select("div.pic2t.pic2t_bg")
		titiles = [title.text for title in title_list if  title.text != None]

		return titiles

		
if __name__ == '__main__':

	PchomeCrawler = Crawler()
	PchomeCrawler.Idle()
	print("==========")
	print(PchomeCrawler.keyword)
	PchomeCrawler.GetPage()
	resulttitle = PchomeCrawler.ParseAndReturnResult()
	for title in resulttitle:
		print(title)
	print("==========")
		




