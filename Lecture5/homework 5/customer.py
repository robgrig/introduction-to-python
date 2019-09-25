from productcheck import check
def buy(product,num,price):
    if check(product,num)==True:
        #nupr=int(num)*int(price)
        print("you bought",product," and spent",num*price)
    else:
        print("sorry! wq are out of thi product")