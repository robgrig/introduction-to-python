import argparse
parser = argparse.ArgumentParser()

parser.add_argument('hamar', type=int)
args = parser.parse_args()
list1 = [3, 5, 9, 2]
c = list1.count(args.hamar)
print(c)