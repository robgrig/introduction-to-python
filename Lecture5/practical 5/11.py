def liter_num(n):
    for x in range(0, n):
        yield (x)

n=int(input("n"))
numbers=[]
numbers.append(liter_num)

numbers=list(numbers)

print(numbers)

#print(liter_num)
for e in numbers:
    print(e)
