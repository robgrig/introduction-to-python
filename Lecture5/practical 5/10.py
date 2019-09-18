def list_els(*list1):
     for i in list1:
        yield (i)

number = list_els([1,2,3,4,5])
for n in number:
    print(n)