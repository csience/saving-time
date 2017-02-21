# coding: utf-8
"""
iref.py
Date:   2/21/2017
Usage:  Run in iOS 10 as a Pythonista 3 app extension module with url input from appex.
Desc:   A simple URL shortener powered by bit.ly for use under Pythonista 3 in iOS 9/10.
Notes:  Pythonista 3 by OMZ-Software required to use included requests and appex modules on iOS.
        Change the access token for analytics purposes.
"""
import requests
import appex

def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    # My bit.ly access token for https://a.ref.sh/ for demonstration purposes. Change this value for your use.
    ACCESS_TOKEN = "c946a815f11eec030dea06056c146115102c1d1d"
    url = "https://api-ssl.bitly.com/v3/shorten"
    querystring = {"access_token": ACCESS_TOKEN}

    appurl = appex.get_url()
    if not appurl:
        print('No input URL found.')
        return
    querystring["longUrl"] = appurl

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
        print((d['data']).get('long_url'))
        print((d['data']).get('url'))

    except ValueError:
        print('JSON decoding failed.')

if __name__ == '__main__':
    main()
