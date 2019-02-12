from dotenv import load_dotenv
import json
import os
import requests

load_dotenv()  # loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable

# see: https://www.alphavantage.co/support/#api-key
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

symbol = "NFLX" # TODO: capture user input

# see: https://www.alphavantage.co/documentation/#daily
# TODO: assemble the request url to get daily data for the given stock symbol

# TODO: issue a "GET" request to the specified url, and store the response in a variable

# TODO: parse the JSON response

# TODO: traverse the nested response data structure to find the latest closing price
latest_price_usd = "$100,000.00"

print("-----------------")
print(f"SYMBOL: {symbol}")
print(f"LATEST DAILY CLOSING PRICE: {latest_price_usd}")
