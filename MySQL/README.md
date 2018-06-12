# MySQL Database
In this section, I'll build databases for the project and provide an introduction in details. Relational database management system (RDBMS) 
is to store and manage large anounts of data, which is based on the relational model, and the data in
the database are processed with the help of mathematical concepts and methods such as set algebra.
Djangp attempts to support as many features as possible on all database backends. MySQL is a RDBMS and
Django provides the unified API for MySQL. In our project, I choose Mysql for web application. And some details are as follows.

## Data preprocess
Our data are from six chinese financial websites. And each line is a json of one document as:

```
doc = {"content":"xxx","source": "xxx", "time": "xxx", "title": "xxx", "url": "xxx"}
```
To get the relational data 
