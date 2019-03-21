import csv
with open ("/Users/nick/Documents/GitHub/geekbrains/Stepik/41/Crimes.csv",'r') as f:
    reader = csv.reader(f)
    cry = {}
    for i in reader:
        if "2015" in i[2]:
            if i[5] in cry:
                cry[i[5]] += 1
            else:
                cry[i[5]] = 1
li = list(cry.items())
li.sort(key = lambda x: -x[1])
print (li[0])

