import os
path = "/Users/nick/Documents/GitHub/geekbrains/Stepik/31/"

def find_in_dir(dir):
    for i in os.listdir(path+dir):
        if os.path.isdir(path+dir+"/"+i):
            find_in_dir(dir+"/"+i)
        if os.path.isfile(path+dir+"/"+i) and i[-3:] == ".py":
            res.add(dir)


res = set()
dir = "main"
find_in_dir (dir)
l = list(res)
l.sort()
print ('\n'.join(l))