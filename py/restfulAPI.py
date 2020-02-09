from flask import Flask
from flask_restful import Resource, Api
import json
from flask_jsonpify import jsonify
import urllib
import ssl
import requests
import csv
app = Flask(__name__)
api = Api(app)
encoding = "utf-8"

def fetchCsvData(url):
	try:
		response = requests.get(url, verify=False)
		print('----------')
		response.encoding = "uft-8"
		print(response.encoding)
		csvData = response.text.strip().split('\n')
		print("typeOfcsvData:")
		print(type(csvData))
		for data in csvData:
			print("typeodData")
			print(type(data))
		return csvData
	except Exception as e:
		print(e)


class Maskdata(Resource):
    def get(self):
        try:
        	urlPath = "http://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D50001-001&l=https://data.nhi.gov.tw/resource/mask/maskdata.csv"
        	lines = fetchCsvData(urlPath)
        	lines = [line.strip() for line in lines]
        	keys = lines[0].split(',') 
        	line_num = 1
        	total_lines = len(lines)
        	datas = []
        	while line_num < total_lines:
        		values = lines[line_num].split(",")
        		datas.append(dict(zip(keys, values)))
        		line_num = line_num + 1
        	# 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
        	print("log!!!!!!!!!!!!!!! 3")
        	json_str = json.dumps(datas, ensure_ascii=False, indent=4)
        	result_data = json_str.replace(r'\"','').replace(r'\\N','').replace(r'\n','')
        	return result_data
        except Exception as e:
        	return e

class Hello_world(Resource):
	def get(self):
		result = "HELLO!"
		return result
api.add_resource(Hello_world, '/')
api.add_resource(Maskdata, '/Maskdata') # Route_1

if __name__ == '__main__':
	print('app run')
	app.run()