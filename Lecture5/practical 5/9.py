def my_dec(func): #my_dec(add_values)
    def wrapper(*args, **kwargs):  #wrapper(*list2)
        
        return func(*args,**kwargs).upper()[0],func(*args,**kwargs)[1:].lower()
    return wrapper


def my_dec2(func):
    def befan():
        return "welcome to the party"+list(func())
    return befan
    


@my_dec2
@my_dec
def flan():
    return "WhiREWRE to everyone"

print(flan())
