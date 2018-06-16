import requests
import time
import re

p = re.compile("[0-9]{14}")

href = 'http://m.10jqka.com.cn'

url = 'https://web.archive.org/__wb/calendarcaptures?url={}&selected_year={}'

times = []
for year in range(2018,2019):
    r = requests.get(url.format(href, year))
    ts = p.findall(r.content)
    for t in ts:
        times.append(t)
    r.close()

p = re.compile("http://.*?/c[0-9]*\.shtml")
start_url = 'https://web.archive.org/web/{}/{}'
for t in times:
    r = requests.get(start_url.format(t, href))
    urls = p.findall(r.content)
    for url in urls:
        print url
    time.sleep(5)
    r.close()
