#Tests with Mempool API
#https://mempool.space/de/docs/api/rest

import requests
import os
from time import sleep

response = requests.get("https://mempool.space/api/v1/difficulty-adjustment")
height = requests.get("https://mempool.space/api/blocks/tip/height")
blocks = requests.get("https://mempool.space/api/blocks")

respond_json = response.json()
height_json = height.json()
blocks_json = blocks.json()

#Status code
#--------------------------------------------------------
status = True
counter = 0
while status == True:
  print("=========API-INFO=========")
  if (response.status_code == 200):
    status = True
    counter += 1       #to check if os.system('clear') works
    print("The request was successful")

  elif (response.status_code == 404):
    status = False
    print("Request failed")

  print("Returned status code: ",response.status_code)
  print("==========================")
  print(counter)
  print("Refresh in 5 seconds...")
  sleep(5)
  if(os.name == 'posix'):
    os.system('clear')
  else:
    os.system('cls')
#------------------------------------------------------
