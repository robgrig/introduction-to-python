res = input ()
import argparse

print (res)


parser = argparse.ArgumentParser()
parser.add_argument("bar1")
parser.add_argument("bar2")
args = parser.parse_args()

lbar1=len(args.bar1)
print("len bar1  = ",lbar1)

if args.bar1 in res:


    print("YES!!, res contains  bar1")   

    res = list(res)  

    index = res.index(args.bar1[1])

    print('The index of bar1:', index)

    print(res)

    
    a=0
    index=index-1
    while a<lbar1:
        #index=index-1
        del res[index]
        print(a)
        a+=1
        print(res)
        
    #print(res)

bar2=list(args.bar2)
res.insert(index, bar2)
print(res)

  