import requests
import re

def links_list(url):
    try:
        req = requests.get(url)
        text = req.text
        pattern = r'<a href=[\"\']([^\'\"]*)[\"\']'
        links = re.findall(pattern, text)
        #print (links)
        return links
    except:
        return []

a = input()
b = input()

#a = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
#b = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
a_links = links_list(a)
find = False
for i in a_links:
    if b in links_list(i):
        find = True
        break

print ("Yes" if find else "No")