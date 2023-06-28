# Bitcoin ticker

This Python script retrieves real-time Bitcoin blockchain information. It provides details such as Bitcoin price, market cap, transaction fees, mempool information, and mining details.

## Features

- Retrieves real-time information about Bitcoin blockchain.
- Plays a sound whenever a new block is mined (support for both Linux and Windows systems).
- Colorful, console-based UI for easy data interpretation.
- Refresh countdown with a progress bar.

## Requirements

- Python 3
- Requests
- Colorama
- TQDM
- Pygame (Linux)
- Winsound (Windows)

## Installation

Clone the repository:

```bash
git clone https://github.com/haui-btc/bitcoin_ticker.git
```

Navigate into the directory:

```bash
cd bitcoin_ticker
```

## Install the requirements:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python bitcoin_ticker.py
```

## Information Provided

The script provides real-time information about:

- Bitcoin Price
- Moscow Time (number of satoshis you can buy at the moment for 1 US Dollar)
- Marketcap
- 24 Hour Volume
- Latest block details (height, timestamp, hash, transaction count, size)
- Mempool Information (unconfirmed transactions, transaction difference from last reload, minimum fee)
- Transaction Fees (low priority, medium priority, high priority)
- Mining Information (difficulty progress, remaining blocks, estimated difficulty change, previous difficulty change)

## Note

- This script uses the APIs from mempool.space and coingecko.com.
- For playing a sound when a new block is mined, it requires Pygame on Linux and Winsound on Windows.
- The sound file to be played should be placed in the 'sound' directory with the name 'sound.mp3'.

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Screenshots

![App Screenshot](https://github.com/haui-btc/bitcoin_ticker/blob/main/screenshots/main.png?raw=true)
![App Screenshot](https://github.com/haui-btc/bitcoin_ticker/blob/main/screenshots/new_block.png?raw=true)
