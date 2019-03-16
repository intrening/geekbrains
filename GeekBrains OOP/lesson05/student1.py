import requests
import re
from bs4 import BeautifulSoup
from collections import Counter


def get_page_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', id='bodyContent').text
    return content


def get_page(url):
    return requests.get(url).text


def get_page_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', id='bodyContent')
    list_of_a = content.find_all(href=re.compile('^\/wiki\/([^\.\:\/]+)$'))
    list_of_links = [a['href'] for a in list_of_a]
    list_of_links = set(list_of_links)
    return list_of_links


def get_common_words(html):
    text = get_page_content(html)
    words = re.findall('[Р°-СЏС‘Рђ-РЇРЃ\-]{3,}', text)
    return words


def get_words_from_links(links):
    words = []
    for link in links:
        if link is not None:
            url = 'https://ru.wikipedia.org' + link
            words += get_common_words(get_page(url))
    return words


def main():
    topic = input('Р’РІРµРґРё С‚РµРјСѓ')
    url = f'https://ru.wikipedia.org/wiki/{topic}'
    main_page = get_page(url)
    main_words = get_common_words(main_page)
    links = get_page_links(main_page)
    main_words += get_words_from_links(links)
    words = Counter(main_words)
    print(words.most_common(10))


main()