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
#API Connection check
status = True

while status == True:
  #Repeats following code if response code==200 (from blocks-api)
  if (blocks.status_code == 200):
    status = True
  # Exit script if response code==404
  elif (blocks.status_code == 404):
    status = False
    print("Lost connection! Exit script")
    os.system('ctrl+c')
  #Print logo
  print(Style.NORMAL + Fore.YELLOW + '''\
  
██████╗ ██╗████████╗ ██████╗ ██████╗ ██╗███╗   ██╗
██╔══██╗██║╚══██╔══╝██╔════╝██╔═══██╗██║████╗  ██║
██████╔╝██║   ██║   ██║     ██║   ██║██║██╔██╗ ██║
██╔══██╗██║   ██║   ██║     ██║   ██║██║██║╚██╗██║
██████╔╝██║   ██║   ╚██████╗╚██████╔╝██║██║ ╚████║
╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝''')
  print(Style.DIM + Fore.LIGHTGREEN_EX + "₿itcoin ticker by https://github.com/haui-btc")
  print()

  #API Endpoints
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
  #Write blockchain API values to lists
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
  #Price/Marketcap
  print(Style.NORMAL + Fore.YELLOW + "==|Price / Marketcap|================================================================")
  print("Price:",round(price.json()["last_trade_price"],2),"USD")
  print()

  #Blockchain Info
  #print index 0 (latest value) from lists
  print(Style.NORMAL + Fore.YELLOW + "==|Blockchain-Info|==================================================================")
  print("Latest block: ",height_list[0])
  print("Timestamp: ",readable_time[0])
  print("Latest block hash:",id_list[0])
  print("Previous block hash:",previous_id_list[0])
  print("TX count:",tx_count_list[0])
  print("Block size:",size_list[0]/1000,"kB")
  print()

  #Mempool Info
  print(Style.NORMAL + Fore.YELLOW + "==|Mempool-Info|=====================================================================")
  print("Unconfirmed TX:",mempool.json()['count'])
  print("Minimum fee:", fees.json()['minimumFee'], "sat")
  print()
  print(Style.NORMAL + Fore.YELLOW + "==|Transaction fees|=================================================================")
  print("Low priority:",fees.json()['hourFee'],"sat")
  print("Medium priority:", fees.json()['halfHourFee'], "sat")
  print("High priority:",fees.json()['fastestFee'],"sat")
  print()

  #Mining info
  print(Style.NORMAL + Fore.YELLOW + "==|Mining-Info|======================================================================")
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

  #Clear screen - check OS to decide if clear or cls is needed
  if (os.name == 'posix'):
    os.system('clear')
  else:
    os.system('cls')