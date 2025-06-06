# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
#read input string

s=input()
result=[]
#to group consecutive characters
for key,group in groupby(s):
    count =len(list(group))
    result.append(f"({count}, {key})")
    
    #print result
print(" ".join(result))