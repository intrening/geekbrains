import re
import sys
s = """blabla is a tandem repetition
123123 is good too
go go
aaa"""
s = s.split('\n')
pattern = r'(\b\w+)\1\b'
for line in sys.stdin:
    line = line.rstrip()
    n = re.match(pattern,line)
    if n and len (n.regs)>1:
        x0 = n.regs[0]
        x1 = n.regs[1]
        if line[x1[0]:x1[1]]*2 == line[x0[0]:x0[1]]:
            print (line)