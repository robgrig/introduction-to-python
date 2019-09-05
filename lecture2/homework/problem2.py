import argparse
parser = argparse.ArgumentParser()
parser.add_argument("tiv")
args = parser.parse_args()
erkarutyun=len(args.tiv)
#print(erkarutyun)
if erkarutyun>=7 and erkarutyun %2!=0:
  s1=int((erkarutyun+1)/2-2)
  s2=int((erkarutyun+1)/2+1)
  print(args.tiv[s1:s2])
  print(args.tiv[:s1]+args.tiv[s1:s2].upper()+args.tiv[s2:])
