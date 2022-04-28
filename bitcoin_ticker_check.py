
from colorama import init, Fore, Back, Style
from tqdm import tqdm
from time import sleep


print(Style.DIM + Fore.LIGHTBLACK_EX + "Reloading data in 15 seconds...")
# Progress bar
pbar = tqdm(total=100, colour="YELLOW")
for i in range(15):
    sleep(1)
    pbar.update(7)
pbar.close()