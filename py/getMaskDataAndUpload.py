from urllib import request
import csv
import json
import time
import autoCommitFileToGit
import ssl


def fetchCsvData(url):
	response = request.urlopen(url)
	#csvObj = csv.reader(response.read("utf-8"))
	return response

def getDataAndUpload():
	encoding = "utf-8"
	ssl._create_default_https_context = ssl._create_unverified_context
	urlPath = "http://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D50001-001&l=https://data.nhi.gov.tw/resource/mask/maskdata.csv"
	response = fetchCsvData(urlPath)
	lines = response.readlines()
	lines = [line.decode(encoding).strip() for line in lines]
	keys = lines[0].split(',') 
	line_num = 1
	total_lines = len(lines)
	# 数据存储
	datas = []
	while line_num < total_lines:
		values = lines[line_num].split(",")
		datas.append(dict(zip(keys, values)))
		line_num = line_num + 1
	# 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
	json_str = json.dumps(datas, ensure_ascii=False, indent=4)
	# 去除\",\\N,\n 无关符号
	result_data = json_str.replace(r'\"','').replace(r'\\N','').replace(r'\n','')
	output_file = "json/maskdata.json"
	# 写入文件
	with open(output_file, "w+", encoding=encoding) as f:
	    f.write(result_data)
	print("convert success")
	autoCommitFileToGit.doCommit()

def keep_gettng_data_and_upload():
	flag = True
	while flag:
		try:
			print("start processing!")
			getDataAndUpload()
			print("uploaded!")
			time.sleep(60)
		except Exception as e:
			print(e)
			flag = False

keep_gettng_data_and_upload()