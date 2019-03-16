import requests
from bs4 import BeautifulSoup as BS

def get_link (topic):
    link = "https://ru.wikipedia.org/wiki/" + topic.capitalize()
    return link

def get_topic_page (link):
    try:
        resp = requests.get(link).text
    except:
        resp = ""
    return resp

def get_list_of_links (topic):
    link = get_link (topic)
    resp = requests.get(link).text
    soup = BS (resp,"html.parser")
    links = soup.findAll('a')
    links_href = [link.get('href') for link in links]
    all_links = set( filter (lambda x: x != None and ("/wiki" or "https://") in x and ".jpg" not in x, links_href))

    full_links = set(filter (lambda x: 'wikipedia.org/wiki' in x, all_links))
    short_links = all_links - full_links
    full_links.update (set ("https://ru.wikipedia.org"+x for x in short_links))
    return full_links