from flask import Flask
from flask_restful import Resource, Api
import json
from flask_jsonpify import jsonify
import urllib
import ssl

app = Flask(__name__)
api = Api(app)

def fetchCsvData(url):
	response = urllib.request.urlopen(url)
	#csvObj = csv.reader(response.read("utf-8"))
	return response


class Maskdata(Resource):
    def get(self):
        encoding = "utf-8"
        ssl._create_default_https_context = ssl._create_unverified_context
        urlPath = "http://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D50001-001&l=https://data.nhi.gov.tw/resource/mask/maskdata.csv"
        response = fetchCsvData(urlPath)
        lines = response.readlines()
        lines = [line.decode(encoding).strip() for line in lines]
        keys = lines[0].split(',') 
        line_num = 1
        total_lines = len(lines)
        #data store
        datas = []
        while line_num < total_lines:
            values = lines[line_num].split(",")
            datas.append(dict(zip(keys, values)))
            line_num = line_num + 1
        json_str = json.dumps(datas, ensure_ascii=False, indent=4)
        result_data = json_str.replace(r'\"','').replace(r'\\N','').replace(r'\n','')
        return result_data

api.add_resource(Maskdata, '/Maskdata') # Route_1

if __name__ == '__main__':
	print('app run')
	app.run(port='5000')