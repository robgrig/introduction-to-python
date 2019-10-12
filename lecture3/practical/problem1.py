import sys
l1 = ['Hallo',1,True]
args = sys.argv[1:]

print(args+l1)
l1.extend(args)
print(l1)