# Mongodb Database
In this section, I'll build databases for the project and provide an introduction in details. Relational database management system (RDBMS) 
is to store and manage large anounts of data, which is based on the relational model, and the data in
the database are processed with the help of mathematical concepts and methods such as set algebra.
Djangp attempts to support as many features as possible on all database backends. MySQL is a RDBMS and
Django provides the unified API for MySQL. In our project, I choose Mysql for web application. And some details are as follows.

## Data preprocess
Our data are from six chinese financial websites, which stored in ../finance_spider folder. And each line is a json of one document as:

```
doc = {"content":"xxx","source": "xxx", "time": "xxx", "title": "xxx", "url": "xxx"}
```
To get the correlation matrix of data in MySQL, I use three .py files to achieve the goal. 
Firstly, I preprocess the data. For all the documents in the dataset, I extract the 'content' from the doc and only analyze the key words excluding 'stop words', such as symbols,preposition,noun and so on, shown as follows:
```
'：' , '。' ， '？' ，'不仅'，'除非','关于'，'充分'，'迟早'，'处处'，'出去'，'成年'，'从未'，'传说'，'匆匆'......
```
All the 'stop words' are list in the stop_words.txt. Using the 'jieba' module, I can get a better chinese word segmentation result for the document. And then I will remove every word in stop_word.txt and keep the main content in the document.
More details are written in preprocess.py. Finally, content information and key words information are stored in ./train_txt/news/ and ./processed_txt/news/ respectively.
```
import jieba.posseg as pseg

# chinese word segmentation
result = []
with open(filename,'r') as f:
    text = f.read()
    words = pseg.cut(text)
for word, flag in words:
    if flag not in stop_flag and word not in stop_words:
        result.append(word)
```

## LDA model
LDA is a generative probabilistic model for collections of discrete data. It is a three-level hierarchical Bayesian model, in which each item of a collection is modeled as a finite mixture over an underlying set of topics. Each topic is modeled as an infinite mixture over an underlying set of a document. For example, if observations are words collected into documents, it posits that each document is a mixture of a small number of topics and that each word's creation is attributable to one of the document's topics. We can apply LDA topic model in learning the topic of each document and label every news with several topics. I realize the LDA topic model in lda_topic.py.
```
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# train lda
lda = LatentDirichletAllocation(n_topics=500, learning_offset=50., random_state=0)
docres = lda.fit_transform(cntTf)
tf_feature_names = cntVector.get_feature_names()
str_topic = []
for topic_idx, topic in enumerate(lda.components_):   
    str_topic_temp = " ".join([tf_feature_names[i] for i in topic.argsort()[:-10 - 1:-1]])
    str_topic_temp2 = str_topic_temp.split(' ')
    str_topic.append(str_topic_temp2[0])
```
I set the related topics of each document as 3 and the final matrix of the whole data is stored in ./relation.txt.

## Gensim
Gensim is a robust open-source vector space modeling and topic modeling toolkit implemented in Python. It aims to handle text collections,using data streaming and efficient incremental algorithms. I import gensim and create a small corpus of the all document and Top-k related news. In gensim, a corpus is simply an object which, when iterated over, returns its documents represented as sparse vectors. Some details are as follows:
```
from gensim import corpora, models, similarities

dictionary = corpora.Dictionary(corpus)
doc_vectors = [dictionary.doc2bow(text) for text in corpus]
tfidf = models.TfidfModel(doc_vectors)
tfidf_vectors = tfidf[doc_vectors]
```
In this project, I choose Top-5 similar news in the similarity matrix followed by a related topic for each document. Every line in the similarity matrix is described as
```
news_id\
similar_1\
similar_2\
similar_3\
similar_4\
similar_5\
relate_topic\
content 
```
And the results stored in ./similarity_txt and then are uploaded to our Mongodb database. 
## Mongodb Startup
Mongodb is an open-source document database that provides high performance, high availability, and automatic scaling.
A record in MongoDB is a document, which is a data structure composed of field and value pairs. MongoDB documents are similar to JSON objects. The values of fields may include other documents, arrays of document. An example is as follows:
```
{
     name: "sue",
     age: 26,
     status: "A"
     groups: ["news","sports"]
 }
 '''
 The advantages of using documents are:
 Document correspond to native data types in many programming languages.
 Embedded documents and arrays reduce need for expensive joins.
 Dynamic schema supports fluent polymorphism.
