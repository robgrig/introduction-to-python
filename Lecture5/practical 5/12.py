def power(max1):
    for x in range(0, max1):
        yield (2**x)
a=power(4)
for i in a:
    print(i) 