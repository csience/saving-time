#!/usr/bin/env python3
"""
ref.py
Date:   2/21/2017
Usage:  python3 ref.py [URL to be shortened]
Desc:   A simple URL shortener optimized for usage at command line and powered by bit.ly.
Notes:  To use in a manner such as: 'ref http://www.example.com/some/long/path/helloWorld.eg.md5'
        modify fd to be an executable and copy the file as 'ref' into '/bin/'.
"""
import requests, sys

# My bit.ly access token for https://a.ref.sh/ for demonstration purposes. Change this value for your use.
ACCESS_TOKEN = "c946a815f11eec030dea06056c146115102c1d1d"
url = "https://api-ssl.bitly.com/v3/shorten"
querystring = {"access_token":ACCESS_TOKEN}

# logic implementation for usage at command line
if len(sys.argv) > 2: exit();
elif len(sys.argv) == 2: querystring["longUrl"] = sys.argv[1]
else: querystring["longUrl"] = "https://twitter.com/mikenkang"

# HTTP header(s)
headers = {
    'cache-control': "no-cache"
    }

# GET HTTP request to bit.ly API stored in requests.request object
response = requests.request("GET", url, headers=headers, params=querystring)

# decode as JSON formatted text from requests.request object to dict
try:
    d = response.json()
    # Print shortened url to console.
    print((d['data']).get('url'))
except ValueError:
    print('JSON decoding failed.')