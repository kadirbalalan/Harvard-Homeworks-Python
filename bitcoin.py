import requests
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response_json = response.json()
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
btc = sys.argv[1]
usdd = response_json["bpi"]["USD"]["rate"]
usd = float(usdd.replace((","), ("")))
try:
    amount = float(btc) * float(usd)
except ValueError:
    sys.exit("Command-line argument is not a number")
try:
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit()
