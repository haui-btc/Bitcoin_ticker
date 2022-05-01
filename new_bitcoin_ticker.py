import requests
import time
import os
from colorama import init, Fore, Back, Style
from tqdm import tqdm
from time import sleep
# For colored strings
init(autoreset=True)
# -----------------------------------------------------------------------------
# Create lists to store values from 'blocks' api
height_list = []
id_list = []
previous_id_list = []
timestamp_list = []
readable_time = []
tx_count_list = []
size_list = []
# Used to calculate mempool tx difference since last reload
mempool_history = []
# -----------------------------------------------------------------------------
# API Connection check / Script loop
# Define API Endpoint for connection check
blocks = requests.get("https://mempool.space/api/blocks")
status = True
while status == True:
    # Repeats following code if response code==200 (from blocks-api)
    if (blocks.status_code == 200):
        status = True
    # Exit script if response code==404
    elif (blocks.status_code == 404):
        status = False
        print("Lost connection! Exit script")
        os.system('ctrl+c')
    # -----------------------------------------------------------------------------
    # Print logo
    print(Style.NORMAL + Fore.YELLOW + '''\
    
    ██████╗ ██╗████████╗ ██████╗ ██████╗ ██╗███╗   ██╗
    ██╔══██╗██║╚══██╔══╝██╔════╝██╔═══██╗██║████╗  ██║
    ██████╔╝██║   ██║   ██║     ██║   ██║██║██╔██╗ ██║
    ██╔══██╗██║   ██║   ██║     ██║   ██║██║██║╚██╗██║
    ██████╔╝██║   ██║   ╚██████╗╚██████╔╝██║██║ ╚████║
    ╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝''')
    print(Style.DIM + Fore.LIGHTBLACK_EX + "₿itcoin ticker by https://github.com/haui-btc")
    print()
    # -----------------------------------------------------------------------------
    # API Endpoints
    # -----------------------------------------------------------------------------
    # Mining
    mining = requests.get("https://mempool.space/api/v1/difficulty-adjustment")
    # Mempool
    mempool = requests.get("https://mempool.space/api/mempool")
    fees = requests.get("https://mempool.space/api/v1/fees/recommended")
    # Bitcoin price / Marketcap
    cap = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")
    blocks = requests.get("https://mempool.space/api/blocks")
    # -----------------------------------------------------------------------------

    # Write blockchain API (blocks) values to list
    # blocks api returns info of the last 10 blocks
    # write values to a list to print only the latest value
    for data in blocks.json():
        height_list.append(data['height'])
        id_list.append(data['id'])
        previous_id_list.append(data['previousblockhash'])
        timestamp_list.append(data['timestamp'])
        tx_count_list.append(data['tx_count'])
        size_list.append(data['size'])
    # -----------------------------------------------------------------------------
    # Convert timestamp to human-readable time
    for times in timestamp_list:
        a = time.ctime(times)
        readable_time.append(a)
    # -----------------------------------------------------------------------------
    # Screen Output
    # -----------------------------------------------------------------------------
    # Price/Marketcap
    print(
        Style.NORMAL + Fore.YELLOW + "==|Price / Marketcap|================================================================")
    print("Price:", round(cap.json()['bitcoin']['usd'], 2), "USD")
    print("Marketcap:", round(cap.json()['bitcoin']['usd_market_cap'], 2), "USD")
    print("24h volume:", round(cap.json()['bitcoin']['usd_24h_vol'], 2), "USD")
    print("24h change:", round(cap.json()['bitcoin']['usd_24h_change'], 2), "USD")
    print()

    # Blockchain Info
    # print index 0 from lists to get the latest value
    print(
        Style.NORMAL + Fore.YELLOW + "==|Blockchain-Info|==================================================================")
    print("Latest block: ", height_list[0])
    print("Timestamp: ", readable_time[0])
    print("Latest block hash:", id_list[0])
    print("Previous block hash:", previous_id_list[0])
    print("TX count:", tx_count_list[0])
    print("Block size:", size_list[0] / 1000, "kB")
    print()

    # Mempool Info
    # Variables for tx-difference
    mempool_tx = mempool.json()['count']
    add = mempool_history.append(mempool_tx)
    second_last = 0
    diff = 0

    # Calculate new TX since last update
    # diff = 0 if
    for i, tx in enumerate(mempool_history[:-1]):
        second_last = tx
        if second_last < mempool_tx:
            diff = int(mempool_tx) - int(second_last)
        else:
            diff = 0
            second_last = Style.NORMAL + Fore.YELLOW + str("New block!")
    print(
        Style.NORMAL + Fore.YELLOW + "==|Mempool-Info|=====================================================================")
    print("Unconfirmed TX:", mempool.json()['count'])
    print("New TX since last reload:", Style.NORMAL + Fore.YELLOW + str(diff) , "(before: " + str(second_last) + ")")
    print("Minimum fee:", fees.json()['minimumFee'], "sat")
    print()

    # Transacation fees
    print(
        Style.NORMAL + Fore.YELLOW + "==|Transaction fees|=================================================================")
    print("Low priority:", fees.json()['hourFee'], "sat")
    print("Medium priority:", fees.json()['halfHourFee'], "sat")
    print("High priority:", fees.json()['fastestFee'], "sat")
    print()

    # Mining info
    print(
        Style.NORMAL + Fore.YELLOW + "==|Mining-Info|======================================================================")
    print("Difficulty progress:", round(mining.json()['progressPercent'], 2), "%")
    print("Remaining blocks:", mining.json()['remainingBlocks'])
    print("Estimated difficulty change:", round(mining.json()['difficultyChange'], 2), "%")
    print("Previous difficulty change:", round(mining.json()['previousRetarget'], 2), "%")
    print()
    # -----------------------------------------------------------------------------
    # Refresh countdown
    print(Style.DIM + Fore.LIGHTBLACK_EX + "Reloading data...")
    # Progress bar
    pbar = tqdm(total=100)  #PARAMS: , colour="white"
    for i in range(15):
        sleep(1)
        pbar.update(7)
    pbar.close()
    # -----------------------------------------------------------------------------
    # Clear screen - check OS to decide if clear or cls is needed
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')