import sys
print('Arguments:', str(sys.argv[1:]))
b=sys.argv[1]
a={1, 3, 4, 5, 7, 'Alice'}
#a.add(b)  #mi tvi hamar
a = a.union(set(sys.argv[1:]))  # mi qani arjeqi depqum
print(a)