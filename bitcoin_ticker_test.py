import requests
import time
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

#API Endpoints
#-----------------------------------------------------------------------------
#Mining
mining = requests.get("https://mempool.space/api/v1/difficulty-adjustment")
#Blockchain
blocks = requests.get("https://mempool.space/api/blocks")
#Mempool
mempool = requests.get("https://mempool.space/api/mempool")
fees = requests.get("https://mempool.space/api/v1/fees/recommended")
#Bitcoin price
price = requests.get("https://api.blockchain.com/v3/exchange/tickers/BTC-USD")
#-----------------------------------------------------------------------------
#Create lists
height_list = []
id_list = []
previous_id_list = []
timestamp_list = []
readable_time = []
tx_count_list = []
size_list = []
#-----------------------------------------------------------------------------


# API Endpoints
#-----------------------------------------------------------------------------
#Mining
mining = requests.get("https://mempool.space/api/v1/difficulty-adjustment")
#Blockchain
blocks = requests.get("https://mempool.space/api/blocks")
#Mempool
mempool = requests.get("https://mempool.space/api/mempool")
fees = requests.get("https://mempool.space/api/v1/fees/recommended")
# itcoin price
price = requests.get("https://api.blockchain.com/v3/exchange/tickers/BTC-USD")
#-----------------------------------------------------------------------------

#Write API values to lists
for data in blocks.json():
  height_list.append(data['height'])
  id_list.append(data['id'])
  previous_id_list.append(data['previousblockhash'])
  timestamp_list.append(data['timestamp'])
  tx_count_list.append(data['tx_count'])
  size_list.append(data['size'])
#-----------------------------------------------------------------------------
#Convert timestamp to readable time
for times in timestamp_list:
  a = time.ctime(times)
  readable_time.append(a)
#-----------------------------------------------------------------------------
#Screen Output
#-----------------------------------------------------------------------------
print(Style.NORMAL + Fore.YELLOW + "==|₿itcoin|===========================================================")
print("Price:",round(price.json()["last_trade_price"],2),"USD")
print()

#Blockchain Info
print(Style.NORMAL + Fore.YELLOW + "==|₿lockchain-Info|===================================================")
print("Latest block: ",height_list[0])
print("Timestamp: ",readable_time[0])
print("Latest block hash:",id_list[0])
print("Previous block hash:",previous_id_list[0])
print("TX count:",tx_count_list[0])
print("Block size:",size_list[0]/1000,"kB")
print()

#Mempool Info
print(Style.NORMAL + Fore.YELLOW + "==|Mempool-Info|======================================================")
print("Unconfirmed TX:",mempool.json()['count'])
print("Minimum fee:",fees.json()['minimumFee'],"sat")
print("Fastest fee:",fees.json()['fastestFee'],"sat")
print()

#Mining info
print(Style.NORMAL + Fore.YELLOW + "==|Mining-Info|=======================================================")
print("Difficulty progress:",round(mining.json()['progressPercent'],2),"%")
print("Remaining blocks:",mining.json()['remainingBlocks'])
print("Estimated difficulty change:",round(mining.json()['difficultyChange'],2),"%")
print("Previous difficulty change:",round(mining.json()['previousRetarget'],2),"%")
print()
#-----------------------------------------------------------------------------

#Refresh countdown
for i in range(15, 0, -1):
  print(Style.DIM + Fore.LIGHTCYAN_EX + "Refresh in",Style.DIM + Fore.YELLOW + f"{i}",Style.DIM + Fore.LIGHTCYAN_EX + "seconds", end="\r", flush=True)
  time.sleep(1)

#Clear screen - check OS to decide if clear or cls
if (os.name == 'posix'):
  os.system('clear')
else:
  os.system('cls')