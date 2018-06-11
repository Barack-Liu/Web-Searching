import jieba.posseg as pseg
import codecs
from gensim import corpora, models, similarities
import jieba
import numpy as np
num = 9225
def tokenization(filename):
    result = []
    with open(filename, 'r') as f:
        text = f.read()
        words = pseg.cut(text)
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result


stop_words = "./stop_words.txt"
stopwords = codecs.open(stop_words,'r',encoding='gbk').readlines()
stopwords = [ w.strip() for w in stopwords ]
stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']




corpus = []
for i in range(num):
    
    filename = './train_txt/news_' + str(i) + '.txt'

    result = tokenization(filename)
    
    corpus.append(result)        
    
dictionary = corpora.Dictionary(corpus)
doc_vectors = [dictionary.doc2bow(text) for text in corpus]
tfidf = models.TfidfModel(doc_vectors)
tfidf_vectors = tfidf[doc_vectors]

similar_matrix = np.zeros([num,6])

for i in range(num):
    
    filename = './train_txt/news_' + str(i) + '.txt'
    query = tokenization(filename)
    query_bow = dictionary.doc2bow(query)
    index = similarities.MatrixSimilarity(tfidf_vectors)
    sims = index[query_bow]
    ans = sorted(enumerate(sims), key=lambda item: -item[1])
    for j in range(6):
        similar_matrix[i,j] = ans[j][0]
                
    

np.save('similar_matrix.npy',similar_matrix)
