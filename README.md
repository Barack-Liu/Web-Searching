# Web-Searching

## Environment
Ubuntu 16.x<br>
python 3.x<br>
MongoDB (db version 2.6.x)<br>
NodeJs 10.x<br>
bootstrap<br>
koa2<br>

## 	Execution
1.cd finance_web && npm install &nbsp;&nbsp; This process is to install the neccessary modules. It's only needed at the first execution.<br>
2.cd finance_spider/ && ./start.sh  &nbsp;&nbsp; This process is to craw the news. The news data will be save into a collection "news" in the mongoDB database "newsSpider". When users log in, another collection "users" will be created in the database "newsSpider".<br>
3.cd finance_web && npm start  &nbsp;&nbsp; This process is to start the local server.<br>
4.surf on http://localhost:3000/ to view website demo &nbsp;&nbsp; Now the website demo should function well.<br>


## Homepage categories

新浪财经-sina  <br> 
同花顺财经-a10jqka  <br> 
腾讯财经-qq  <br> 
中国证券网-cnstock <br> 
搜狐财经-sohu <br>
东方财富网-eastmoney<br>
All the financial news is roughly divided into 6 categories according to the source website of the news.<br>


## Database Structure
The name of the database: newsSpider. See Web-Searching\Front-End Image\F10.png<br>
There are two tables in the database:news and users.See Web-Searching\Front-End Image\F11.png<br>
The structure of table "news".See Web-Searching\Front-End Image\F9.png<br>
The structure of table "users".See Web-Searching\Front-End Image\F8.png<br>


## Update Record
0616-LHY-I need to integrate the three parts of project Report. And then I need to connect the front-end with the data that the back-end provide.<br>
0615-LHY-I have finished the front-end Project Report. XRC has finished the MongoDB database and I need to connect the back-end with the database.<br>
0614-LHY-When I crawl some new data today, the demo website still present the news crawed yesterday. I suspect that this issue may be caused by the reason that the newsSpider builts a new MongoDB database but the website still query for the old one. I will try to fix it.<br>
0613-LHY-Requirement0,R2,R3,R4 and R5 are finished. The remaining task is to achive R1 and change database from MySQL to MongoDB<br>
0612-LHY-Now the front-end read data from MongDB, we need XRC to modify it to read data from MySQL<br>
0611-LHY-Website demo running. I need to connect to DB and develop searching function

## Project Description
In this project, you are asked to build a simple financial news website. All your data should be crawled from the following websites. These are some Chinese financial news websites. Note that for each website we give, you need to crawl all the news starting from year 2015 (including 2015) up to now.

## Data format
Your data should be stored in plain text format. Each line should be a json of one document. For each document json should be like, doc= {“content”: “xxx”, “source”: “xxx”, “time”: “xxx”, “title”: “xxx”, “url”: “xxx”}.


## Project requirements
0. (Basic) For each website we give, you need to crawl all the news starting from year 2015 (including 2015) up to now.
1. (about 30% scores) Support several search methods. Firstly, user can just input some keywords, you need to search these keywords in the whole database and return a list of news. Secondly, user can choose search in the title or search in everywhere. Thirdly, users can limit which year of news they want when doing search. 
2. (about 20% scores) Manually design or automatic generate proper categories and classify the crawled news into those categories. 
3. (about 30% scores) Support news recommendation. After reading one or more piece of news, you need to find topics which are interesting for this user and recommend some piece of news. 
4. (about 20% scores) Your system should work in real-times. This means when one of the above websites publish new articles, you can catch them into your system with little delay. 
5. (Bonus) Allow users to track some topics. When your system finds some latest articles, which are related to one of these topics, you need to generate a new web page which arranges these related articles in a good manner. Then you need to send this generated web page to user’s email. 

## Deliverables
The final deliverables should include the following items:<br>
⚫ A well-written report to describe your ideas, design, implementation, example queries and results (with screenshots), conclusion, etc.<br>
⚫ A web demo deployed on any publicly accessible web server (in case you can’t find an accessible machine to host your code and data, you can deploy the server on your local computer and contact Yangyang or Jessie for a personal demo in her office, before the due date).<br>
⚫ Source code of the whole search system.<br>
⚫ Zipped archive of the entire crawled data.<br>

## Task allocation
| Name        |       Task  |
| --------   |  :----: |
| LCY       | Spider Module<br> English Project Document(Word Version)<br> Requirement0<br> R4<br>         |
| LHY        | Website Module<br>English Project Document(Word Version)<br>   R1<br> R2<br>          |
| XRC        | Database Module<br>English Project Document(Word Version)<br>  R3<br> R5<br>      |



## Chinese financial news
http://www.eastmoney.com  
东方财富网  <br> 
http://finance.sina.com.cn   
sina  <br> 
http://www.10jqka.com.cn  
同花顺财经  <br> 
http://finance.qq.com  
腾讯财经  <br> 
http://www.cnstock.com  
中国证券网  <br> 
http://business.sohu.com  
搜狐财经 <br>  


