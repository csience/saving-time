#!/usr/bin/env python2

'''
04-20-2017
Michael N. Kang
Retrieves specific port information from speed guide and outputs it to terminal stdout.
usage: python port.py [PORT_NUMBER]
'''

import sys, urllib2
from bs4 import BeautifulSoup

url = "http://www.speedguide.net/port.php?port="

try:
    port = sys.argv[1];
except:
    quit();
if not port.isalnum():
    print "Enter a port number."
    port = input()

query = url+port
content = urllib2.urlopen(query).read()
soup = BeautifulSoup(content)
table = soup.find("table", attrs={"class":"port"})

# http://stackoverflow.com/questions/11790535/extracting-data-from-html-table
headings = [th.get_text() for th in table.find("tr").find_all("th")]
'''
for th in table.find("tr").find_all("th"):
    headings.append(th.get_text())
'''
datasets = []
for row in table.find_all("tr")[1:]:
    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
    datasets.append(dataset)

for dataset in datasets:
    for field in dataset:
        print "{0:<16}: {1}".format(field[0], field[1])

'''
line 230 is start of port table <table class="port">
http://stackoverflow.com/questions/11790535/extracting-data-from-html-table
'''