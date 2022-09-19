# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input().strip()
pattern = r'(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})(?=[bcdfghjklmnpqrstvwxyz])'

result = re.findall(pattern, s, re.IGNORECASE)

if result:
    for rslt in result:
        print(rslt)
else:
    print(-1)
    