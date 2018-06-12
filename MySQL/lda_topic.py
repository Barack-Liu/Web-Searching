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
num = 25083
#
#
# according to output of preprocess.py

def tokenization(filename):

	'''
	parameter: txt path
	return: str list, delete stop words
	'''
	result = []
	with open(filename,'r',encoding='utf-8') as f:
		text = f.read()
		words = pseg.cut(text)

	for word, flag in words:
		if flag not in stop_flag and word not in stop_words:
			result.append(word)

	return result


#LDA model

#conver stop words to list
stpwrdpath = "./stop_words.txt"
stpwrd_dic = open(stpwrdpath, 'rb')
stpwrd_content = stpwrd_dic.read()  
stpwrdlst = stpwrd_content.splitlines()
stpwrd_dic.close()


#conver word to word vector
res = ['x' for n in range(num)]
for i in range(num):
    processed_txtpath = './processed_txt/news_' + str(i) + '.txt'
    with open(processed_txtpath,'r',encoding='utf-8') as f:
        res[i] = f.read()
cntVector = CountVectorizer(stop_words=stpwrdlst)
cntTf = cntVector.fit_transform(res)


#train lda
lda = LatentDirichletAllocation(n_topics=500,
                                learning_offset=50.,
                                random_state=0)
docres = lda.fit_transform(cntTf)# num*n_topics matrix , weight of topics in each news


#print hign weighted term in each topic
tf_feature_names = cntVector.get_feature_names()
str_topic = []
for topic_idx, topic in enumerate(lda.components_):
    print('Topic #%d: '%topic_idx)
    str_topic_temp = " ".join([tf_feature_names[i]
                        for i in topic.argsort()[:-10 - 1:-1]])
    print(str_topic_temp)
    str_topic_temp2 = str_topic_temp.split(' ')
    str_topic.append(str_topic_temp2[0])

#create matrix: row - news,column - topic

#relate_topic = np.zeros([num,2])
relate_topic = [[0 for i in range(3)] for j in range(num)]
for i in range(num):
	topic = np.where(docres[i,:] == np.max(docres[i,:]))
	topic = topic[0]
	relate_topic[i][0] = i
	relate_topic[i][1] = topic[0]
	relate_topic[i][2] = str_topic[int(topic[0])]

print(relate_topic[0:10])


with open('relation.txt','w',encoding='utf-8') as f:
    for i in range(num):
        each_relation = relate_topic[i][0:3:2]
        for r in each_relation:
            f.write(str(r))
            f.write('  ')
        f.write('\n')