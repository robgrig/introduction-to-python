list1=["anna","edgar"]

def my_dec(func): #my_dec(add_values)
    def wrapper(*args, **kwargs):  #wrapper(*list2)
        print(list1)
        print(func(*args,**kwargs))
    return wrapper


@my_dec
def add_values(*list2):
    for x in list2:
        list1.append(x)
    return list1

add_values(1,3,5)