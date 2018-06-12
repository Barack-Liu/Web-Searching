# MySQL Database
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
All the 'stop words' are list in the stop_words.txt. I will remove every word in stop_word.txt and keep the main content in the document.
More details are written in preprocess.py. Finally, content information and key words information are stored in ./train_txt/news/ and ./processed_txt/news/ respectively.

# LDA topic model
LDA is a generative probabilistic model for collections of discrete data. It is a three-level hierarchical Bayesian model, in which each item of a collection is modeled as a finite mixture over an underlying set of topics. Each topic is modeled as an infinite mixture over an underlying set of a document. For example, if observations are words collected into documents, it posits that each document is a mixture of a small number of topics and that each word's creation is attributable to one of the document's topics. We can apply LDA topic model in learning the topic of each document and easily recommend some related news in the same topic. I realize the LDA topic model in tf.idf_recommend.py
