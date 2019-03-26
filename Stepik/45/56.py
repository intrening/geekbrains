#n = input()
n = '1984'
arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman = "M CM D CD C XC L XL X IX V IV I".split()

for i in range(len(n)):
    q = int(n[i])*int(10**(len(n)-i-1))
    j = 0
    while q !=0:        
        if q>=arab[j]:
            res = roman[j]*(int(q//arab[j]))
            q = q%arab[j]
            print (res,end='')
        j+=1