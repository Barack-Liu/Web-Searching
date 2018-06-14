#py35
import numpy as np
import json
import os
import unicodedata
import jieba
import codecs
import jieba.posseg as pseg
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def tokenization(filename):

	'''
	parameter: txt path
	return: str list, delete stop words
	'''
	result = []
	with open(filename,'r') as f:
		text = f.read()
		words = pseg.cut(text)

	for word, flag in words:
		if flag not in stop_flag and word not in stop_words:
			result.append(word)

	return result



#read data from json
with open('./data/test/easymoney.json','r') as f:
	raw_data1 = json.load(f)
with open('./data/test/sina.json','r') as f:
	raw_data2 = json.load(f)
with open('./data/test/a10jqka.json','r') as f:
	raw_data3 = json.load(f)

raw_data = raw_data1 + raw_data2 + raw_data3

#write raw data to txt
num = len(raw_data)
print('total news: ',num)
for i in range(num):

	content = raw_data[i]['content']
	content = unicodedata.normalize('NFKD',content)
	content = content[0:-40] #delete useless char at end

	#create path to save txt data from raw data
	txt_path = './train_txt/news_' + str(i) + '.txt'
	if not os.path.exists(os.path.split(txt_path)[0]):
		os.makedirs(os.path.split(txt_path)[0])

	with open(txt_path, 'w') as f:
		f.write(content)



#process txt with jieba and delete stop_words
stop_words = './stop_words.txt'
stopwords = codecs.open(stop_words,'r',encoding='gbk').readlines()
stopwords = [ w.strip() for w in stopwords]
stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']



for i in range(num):
	filename = './train_txt/news_' + str(i) + '.txt'
	result = tokenization(filename)
	result = '   '.join(result)

	processed_txtpath = './processed_txt/news_' + str(i) + '.txt'
	if not os.path.exists(os.path.split(processed_txtpath)[0]):
		os.makedirs(os.path.split(processed_txtpath)[0])

	with open(processed_txtpath, 'w') as f:
		f.write(result)
