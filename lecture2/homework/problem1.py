import argparse
import time
import datetime
parser = argparse.ArgumentParser()
parser.add_argument("--year",type=int)
parser.add_argument("--day",type=int)
args = parser.parse_args()
today = datetime.date.today()
print(today)

#if args.year and args.day:
that_year = datetime.timedelta(days=365*args.year)
that_day = datetime.timedelta(days = args.day)


print( today + that_day)
#print('Day: ', datetime.date.today().day)