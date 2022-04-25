import requests

#API Endpoints
#-----------------------------------------------------------------------------
#Marketcap
cap = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")
#-----------------------------------------------------------------------------

print(cap.json())
print("Marketcap:",round(cap.json()['bitcoin']['usd_market_cap'],2))