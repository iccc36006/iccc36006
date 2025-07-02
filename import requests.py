import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
price = requests.get(url).json()['ethereum']['usd']
print(f"Current ETH price: ${price}")