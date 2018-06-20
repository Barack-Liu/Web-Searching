import requests
import time
import re

p = re.compile("[0-9]{14}")

href = 'https://finance.qq.com'

url = 'https://web.archive.org/__wb/calendarcaptures?url={}&selected_year={}'

times = []
for year in range(2015,2019):
    r = requests.get(url.format(href, year))
    ts = p.findall(r.content)
    for t in ts:
        times.append(t)
    r.close()

#print 'time collect over'

p = re.compile("http://finance.qq.com.*?/a/[0-9]*/[0-9]*\.htm")
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
