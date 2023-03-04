#! /usr/bin/env python3
# coding:utf-8

import json

file = "csv_data.txt"
datas = []
f = open(file,'r',encoding='utf-8')
lines = f.readlines()
f.close()

#读取标题

title_fields = [str(e).strip() for e in lines[0].split("\t")]

for line in lines[1:]:
	values = [str(e).strip() for e in line.split('\t')];
	data = {}
	for i in range(len(values)):
		key = title_fields[i]
		value = values[i]
		data[key] = value
	datas.append(data)


print(datas)

# text = json.dumps(datas)
# print(text)