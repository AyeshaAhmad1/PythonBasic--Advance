import argparse
import requests

parser = argparse.ArgumentParser(description="Download a file from the internet")

parser.add_argument("url", help="File URL")
parser.add_argument("output", help="Name of the saved file")

args = parser.parse_args()

response = requests.get(args.url)

with open(args.output, "wb") as file:
    file.write(response.content)

print(f"File downloaded as {args.output}")
