# import sources
import requests
import useragent
from bs4 import BeautifulSoup
from lxml.html import fromstring
from itertools import cycle
import traceback
import random
from collections import OrderedDict
from fake_useragent import UserAgent
from pprint import pprint


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def test_proxy():
    proxies = get_proxies()
    print(proxies)
    proxy_pool = cycle(proxies)
    working_proxies = set()

    url = 'https://httpbin.org/ip'
    for i in range(1, 11):
        # Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d" % i)
        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy})
            print(response.json())
            working_proxies.add(proxy)
        except:
            # Most free proxies will often get connection errors. You will have retry the entire request using
            # another proxy to work. We will just skip retries as its beyond the scope of this tutorial and we are
            # only downloading a single url
            print("Skipping. Connnection error")
    print(working_proxies)
    return working_proxies


def get_header():
    ua = UserAgent()
    ua_list = [ua.safari, ua.ff, ua.firefox, ua.google, ua.chrome, ua.opera, ua.msie, ua.ie]
    agent = random.choice(ua_list)
    # print(agent)
    return agent


def test_header():
    user_agent_list = []
    for i in range(1, 11):
        user_agent_list.append(get_header())

    # Print the test agents
    url = 'https://httpbin.org/headers'
    for i in range(1, 4):
        # Pick a random user agent
        user_agent = random.choice(user_agent_list)
        # Set the headers
        headers = {'User-Agent': user_agent}
        # Make the request
        response = requests.get(url, headers=headers)

        print("Request #%d\nUser-Agent Sent:%s\n\nHeaders Received by HTTPBin:" % (i, user_agent))
        print(response.json())
        print("-------------------")

    headers_list = [
        # Firefox 77 Mac
        {
            "User-Agent": random.choice(user_agent_list),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        },
        # Firefox 77 Windows
        {
            "User-Agent": random.choice(user_agent_list),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        },
        # Chrome 83 Mac
        {
            "Connection": "keep-alive",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": random.choice(user_agent_list),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                      "application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        },
        # Chrome 83 Windows
        {
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": random.choice(user_agent_list),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                      "application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"
        }
    ]
    print(headers_list)

    # Create ordered dict from Headers above
    ordered_headers_list = []
    for headers in headers_list:
        h = OrderedDict()
        for header, value in headers.items():
            h[header] = value
        ordered_headers_list.append(h)

    url = 'https://httpbin.org/headers'

    headers_pool = cycle(headers_list)
    for i in range(1, 5):
        # Pick a random browser headers
        headers = next(headers_pool)
        # Create a request session
        r = requests.Session()
        r.headers = headers

        response = r.get(url)
        print("Request #%d\nUser-Agent Sent:%s\n\nHeaders Recevied by HTTPBin:" % (i, headers['User-Agent']))
        print(response.json())
        print("-------------------")

    # print(headers_list)
    return headers_list


def get_link():
    header_list = test_header()
    header = random.choice(header_list)
    print(header)
    proxy = test_proxy()
    print(proxy)
    url = "https://www.youtube.com/watch?v=zWmZhWCazw0&list=PLsaURXf-TfmS2QzlvQcYBl7D02kvfqRIp&ab_channel=DubstepGutter"
    playlist_link = requests.get(url, proxies={"http": proxy, "https": proxy}, headers=header)
    playlist_content = playlist_link.content
    print(playlist_content)


# test_header()
get_link()
'''
#get Link
playlist_link = requests.get("https://www.youtube.com/watch?v=zWmZhWCazw0&list=PLsaURXf-TfmS2QzlvQcYBl7D02kvfqRIp&ab_channel=DubstepGutter", proxies = proxies={"http": proxy, "https": proxy}, headers = headers)
playlist_content = playlist_link.content
#print(playlist_content)

#parse into Beautifulsoup Object
dsgplaylist = BeautifulSoup(playlist_content, "html.parser")
print(dsgplaylist)

#Select all Youtube Video Links
videoLinks = dsgplaylist.find_all('div', id='playlist-items')
print(videoLinks)

#Content Management / Creating Lists
'''
