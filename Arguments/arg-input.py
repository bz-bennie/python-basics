import argparse

parser = argparse.ArgumentParser(description="Add two Numbers")
parser.add_argument("first", help="first number", type=str)
parser.add_argument("second", help="second number", type=str)
args= parser.parse_args()

print(args)

string_answer = args.first + args.second
print(string_answer)

int_answer = int(args.first) + int(args.second)
print(int_answer)