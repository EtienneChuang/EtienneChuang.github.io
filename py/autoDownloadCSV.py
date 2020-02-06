import operator
import urllib.request as request
import json
import csv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def fetch_data2(url):
	tempDict = {}
	urlResp = request.urlopen(url)
	result = csv.reader(urlResp.read().decode('utf-8')) 
	return result

def getList():
	stockList = []
	stockDict = dict({'code':'9904','name':'寶成'})
	stockList.append(stockDict)
	stockDict = dict({'code':'9938','name':'百和'})
	stockList.append(stockDict)
	return stockList

def getCsvToJson(csvFile):
	jsonfile = open('file.json', 'w')
	fieldnames = ("醫事機構代碼","醫事機構名稱","醫事機構地址","醫事機構電話","成人口罩總剩餘數","兒童口罩剩餘數","來源資料時間")
	reader = csv.DictReader(csvFile, fieldnames)
	for row in reader:
	    json.dump(row, jsonfile)
	    jsonfile.write('\n')

csvUrl = "http://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D50001-001&l=https://data.nhi.gov.tw/resource/mask/maskdata.csv"
r = fetch_data2(csvUrl)
for row in r:
	print(row)





#url = "http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=json&date=20190115&stockNo=9904"
#print(fetch_data2(url))