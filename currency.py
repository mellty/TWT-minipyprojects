# Uses a free currency conversion API - freecurrencyapi.com
# tempemail viwocib516@vkr1.com, email was deleted and password is forgotten :(( ip address is there too but hope it's fine..

import requests # already imported via pip

API_KEY = '' # constant valued variable

BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}" # fstring to embed the var in the {}

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]


# function
def convert_currency(base):

    # currencies var list needs to be converted to a string to be used in the fstring
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]


    except Exception as e:
        print(e)
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)

    if not data:
        continue


    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")