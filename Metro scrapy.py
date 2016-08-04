# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  
import os
import csv
import codecs
import multiprocessing
import re
import math
import json
import httplib2
import urllib2
import time
import multiprocessing
import requests
from bs4 import BeautifulSoup

startTime = time.time()


class PageScraper(object):

    def __init__ (self, item_name, city_id, page_num ):


        self.page_num = page_num
        self.item_name = item_name 
        self.url = self.joinURL(item_name,page_num)
        self.cookies = self.getCookies(city_id)
        self.id = self.getCityName(city_id)


    def joinURL(self,item_name,page_num):
        urlFirst= u'http://www.metromall.cn/Product/ProductSearch.aspx?'
        num= str(page_num)
        query = ''.join([u'&pg=', num, u'&KeyWord=',self.item_name])
        url = ''.join([urlFirst,query])
        return url

    def getHTML(self,url):
        headers = {"cookie":str(self.cookies)}
        try:
            http=httplib2.Http()
            response,content=http.request(url,'GET',headers=headers)
            return content
		except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
		    print ('connect error')
			return None

    def parasePage(self):
       
        html = self.getHTML(self.url)
		if html == None:
            return None
        soup = BeautifulSoup(html, 'html.parser')
        div_page = soup.body.find('div',attrs={'id':'page'})
        div_li = div_page.find_all('li')
        return div_li

    def getTotal(self):

        try:

            html = self.getHTML(self.url)
            soup = BeautifulSoup(html, 'html.parser')
            div_page = soup.body.find('div',attrs={'id':'page'})
            div_pic= div_page.find('div', attrs={'class':'fix pro_main'})
            div_li = div_pic.find_all('li')            
            for products in  div_li:
                b = products.find('p',attrs={'class':'name'})
                c = b.a.get_text()  

                d = products.find('div', attrs={'class':'price'})
                e = d.font.get_text()
                finishTime = time.time()
                processingTime = finishTime - startTime         
                print ("complete one set using %d seconds"%processingTime)
                self.makeOutput(self.id, c, e)
        except AttributeError:
            return None        



    def getCookies(self,city_id):
        f = open('cookies.json','r') 
        value = json.load(f)
        getvalue  = value[city_id]
        f.close()
        return getvalue   

    def getCityName(self,city_id):
        f = open('PostStaID.json','r') 
        value = json.load(f)
        getvalue  = value[city_id]
        f.close()
        return getvalue    


    def makeOutput(self,Citylocation,Title,Price):   

        with open(self.item_name+'.csv', 'a+') as writer:         
            writer.write(codecs.BOM_UTF8)  
            writer.write('%s,%s,%s\n' %(Citylocation,Title,Price) )  
            writer.close()


class multiprocess():

    def __init__ (self) :

        self.item = self.getKeywords()
        self.city_id = self.getCities()

    def getCities(self):
        f = open('chosensample.json','r') 
        value = json.load(f)
  
        f.close()
        return value

    def getKeywords(self):
        f = open('keywords.json','r') 
        value = json.load(f)
        getvalue  = value['name']
        f.close()
        return getvalue

    def runScraper1(self):
        item_name = self.item
        city_id1 = self.city_id['set1']
        for id in city_id1:

            scraper1 = PageScraper(item_name, id, 1) 
            scraper1.getTotal()
    def runScraper2(self):
        city_id2 = self.city_id['set2']
        item_name = self.item
        for id in city_id2:

            scraper2 = PageScraper(item_name, id, 1) 
            scraper2.getTotal()
    def runScraper3(self):
        item_name =self.item
        city_id3 = self.city_id['set3']
        for id in city_id3:

            scraper3 = PageScraper(item_name, id, 1) 
            scraper3.getTotal()
    def runScraper4(self):
        item_name = self.item
        city_id4 = self.city_id['set4'] 
        for id in city_id4:

            scraper4 = PageScraper(item_name, id, 1) 
            scraper4.getTotal()    


#----------class definition----------


#----------main function----------
if __name__ == '__main__':


    startTime = time.time()


    multitask = multiprocess()

    p1 = multiprocessing.Process(target = multitask.runScraper1)
    p2 = multiprocessing.Process(target = multitask.runScraper2)
    p3 = multiprocessing.Process(target = multitask.runScraper3)
    p4 = multiprocessing.Process(target = multitask.runScraper4)     
    p1.start()
    p2.start()
    p3.start()
    p4.start()















#----------main function----------
