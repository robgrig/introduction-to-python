pro={"candy":10,"juice":5,"pen":50}
def check(product,num):
    if product in   pro:
        var =pro[product]
        #print(product," value is  "+str(var))
        if num<var:
            #print("lox lava")
            return True 
        else:
            #print("chka")
            return False

#check("candy",3)