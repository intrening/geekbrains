import re
import sys
s = """attraction
buzzzz"""
s = s.split('\n')
#li = sys.stdin
li = s
pattern = r'(\w)\1'
for line in li:
    line = line.rstrip()
    while re.findall (pattern,line):
        line = re.sub(pattern,r"\1",line)
    print (line)
