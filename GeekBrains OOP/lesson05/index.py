#1. Получить common words со страниц, на которые есть ссылки
#Получить ссылки на соседние страницы.
#Спарсить отдельно соседние страницы.
#Сложить все в один список.

import wiki_requests as wiki
import re

def get_topic_words (link):
    html_content = wiki.get_topic_page (link)
    words = re.findall(r"[а-яА-Я\-\']{3,}", html_content)
    return words

def get_common_words (words_list):    
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] +=1
        else:
            rate[word] = 1
    rate_list = list (rate.items())
    rate_list.sort(key = lambda x:-x[1])
    return rate_list

def visualize_common_words(topic):
    link = wiki.get_link (topic)
    words = get_topic_words (link)
    list_links = wiki.get_list_of_links (topic)

    for link in list_links:
        words += get_topic_words (link)

    rate_list = get_common_words (words)
    print ("TOP 10:")
    for i in rate_list[0:9]:
        print (i[0])

def main():
    topic = input("topic?: ")
    visualize_common_words (topic)

main()