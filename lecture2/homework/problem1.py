import argparse
import time
import datetime
parser = argparse.ArgumentParser()
parser.add_argument("--year",type=int)
parser.add_argument("--day",type=int)
args = parser.parse_args()
today = datetime.date.today()
print(today)


that_year = datetime.timedelta(year=args.year)
that_day = datetime.timedelta(days = Day)


print( today + that_year)
#print('Day: ', datetime.date.today().day)