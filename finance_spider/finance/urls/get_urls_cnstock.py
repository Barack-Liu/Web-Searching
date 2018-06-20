import requests
import time
import re

p = re.compile("[0-9]{14}")

href = 'www.cnstock.com'

url = 'https://web.archive.org/__wb/calendarcaptures?url={}&selected_year={}'

times = []
for year in range(2017, 2019):
    r = requests.get(url.format(href, year))
    ts = p.findall(r.content)
    for t in ts:
        times.append(t)
    r.close()

print 'time collect over'

p = re.compile("http://news.cnstock.com/news,[a-z]{2,4}-[0-9]{6}-[0-9]{7}.htm")
start_url = 'http://web.archive.org/web/{}/{}'
for t in times:
    try:
        r = requests.get(start_url.format(t, href))
        #print start_url.format(t, href)
        urls = p.findall(r.content)
        for url in urls:
            print url
        r.close()
    except Exception as e:
        pass
