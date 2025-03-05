import sys

fileName = sys.argv[1]

with open(fileName,'r') as file:
    lines = file.readlines()
    
print("the file has",len(lines),"lines,")