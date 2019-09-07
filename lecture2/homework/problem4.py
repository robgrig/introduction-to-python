import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", type=str)
args = parser.parse_args()

print(args.text)

text=args.text.upper()

print(text.count("USA"))


Z=args.text.replace("USA", "Armenia")
Z=args.text.replace("usa", "Armenia")

print(Z)