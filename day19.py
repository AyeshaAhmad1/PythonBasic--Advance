import argparse

parser = argparse.ArgumentParser(
    description="A simple command-line calculator"
)

parser.add_argument(
    "operation",
    choices=["add", "sub", "mul", "div"],
    help="Operation to perform"
)

parser.add_argument(
    "num1",
    type=float,
    help="First number"
)

parser.add_argument(
    "num2",
    type=float,
    help="Second number"
)

args = parser.parse_args()

if args.operation == "add":
    print(args.num1 + args.num2)

elif args.operation == "sub":
    print(args.num1 - args.num2)

elif args.operation == "mul":
    print(args.num1 * args.num2)

elif args.operation == "div":
    print(args.num1 / args.num2)