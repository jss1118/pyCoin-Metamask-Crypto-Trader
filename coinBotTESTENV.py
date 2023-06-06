#may 23
#starting 2nd attempt
from web3 import Web3
import web3
import http
import secrets
import curses
import math
import os
import itertools
import requests
from colorama import *
import time
from datetime import datetime
import threading
import subprocess
import cryptowatch
import cryptowatch as cw
import sys
import ctypes
from LocalAuthentication import LAContext
from LocalAuthentication import LAPolicyDeviceOwnerAuthenticationWithBiometrics
import json
from playsound import *
from eth_account import account
from web3.exceptions import CannotHandleRequest
from datetime import date
try:
    import pandas_datareader as web
    import datetime as dt
    import yfinance as yf
    import time
    import threading
    import requests
    import datetime
    from datetime import timedelta
    from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
    from web3.auto import w3
    import web3.eth
    from eth_account import Account
    import secrets
    import colorama
    from colorama import Fore, Back, Style
    import os
    from PIL import Image
    import matplotlib.pyplot as plt
    import AppKit
    import Foundation
    from playsound import playsound
    from coinbase.wallet.client import Client
    import bcrypt
    from getpass import getpass
    import boto3
    import ast
    import json
    import websocket._exceptions
    import websocket
    import asyncio
    import sqlite3
    import hashlib
    from bs4 import BeautifulSoup
    from web3 import Web3, middleware
    from web3.gas_strategies.time_based import medium_gas_price_strategy
    import numpy as np
    import pandas as pd
    from pycoingecko import CoinGeckoAPI
    import ta
    import ccxt
    import re
    from datetime import datetime
except:
    pass
#all predefined variables




#CALL LIMIT THREAD






api_fetch_number = 0









touch_id = None
account_connected = False
cw_api_key = 'JCV7WBF0EJXS0TE2JC84'

print("coinBot Testing Environment version 2.0 Alpha")


def write_encrypted_data_to_file(encrypted_data):
    with open("/Users/joshua.stanley/Desktop/   /pycoin/gen 2 (current)/encrypted_data.txt", "a") as file:
        file.write(encrypted_data + "\n")
    print("Encrypted data has been written to encrypted_data.txt.")






def check_file_for_text(text):
    with open("/Users/joshua.stanley/Desktop/   /pycoin/gen 2 (current)/encrypted_data.txt", "r") as file:
        file_contents = file.read()
        if text in file_contents:
            global private_key
            private_key = True
            
        else:
            
            
            private_key = False









def is_connected():
    try:
        # Send an HTTP GET request to google.com
        global internet_connection
        internet_connection = False
        requests.get('https://www.google.com', timeout=5)
        print(Fore.GREEN + "Connected to internet.")
        internet_connection = True
        
    except requests.ConnectionError:
        # Connection error, the user is not connected to the internet
        print(Fore.RED + "Could not connect to internet. Retrying...")
        time.sleep(5)
        while not internet_connection:    
            is_connected()

is_connected()


#check if API is online





kTouchIdPolicy = LAPolicyDeviceOwnerAuthenticationWithBiometrics

c = ctypes.cdll.LoadLibrary(None)

PY3 = sys.version_info[0] >= 3
if PY3:
    DISPATCH_TIME_FOREVER = sys.maxsize
else:
    DISPATCH_TIME_FOREVER = sys.maxint

dispatch_semaphore_create = c.dispatch_semaphore_create
dispatch_semaphore_create.restype = ctypes.c_void_p
dispatch_semaphore_create.argtypes = [ctypes.c_int]

dispatch_semaphore_wait = c.dispatch_semaphore_wait
dispatch_semaphore_wait.restype = ctypes.c_long
dispatch_semaphore_wait.argtypes = [ctypes.c_void_p, ctypes.c_uint64]

dispatch_semaphore_signal = c.dispatch_semaphore_signal
dispatch_semaphore_signal.restype = ctypes.c_long
dispatch_semaphore_signal.argtypes = [ctypes.c_void_p]


def is_available():
    context = LAContext.new()
    return context.canEvaluatePolicy_error_(kTouchIdPolicy, None)[0]


def touch_id_authenticate(reason='authenticate via Touch ID'):
    context = LAContext.new()

    can_evaluate = context.canEvaluatePolicy_error_(kTouchIdPolicy, None)[0]
    if not can_evaluate:
        touch_id = False
    else:
        touch_id = True

    sema = dispatch_semaphore_create(0)

    # we can't reassign objects from another scope, but we can modify them
    res = {'success': False, 'error': None}

    def cb(_success, _error):
        res['success'] = _success
        if _error:
            res['error'] = _error.localizedDescription()
        dispatch_semaphore_signal(sema)

    context.evaluatePolicy_localizedReason_reply_(kTouchIdPolicy, reason, cb)
    dispatch_semaphore_wait(sema, DISPATCH_TIME_FOREVER)

    if res['error']:
        raise Exception(res['error'])

    return res['success']
def password_authenticate():
    command = ['sudo', '-v']
    try:
        subprocess.check_call(command, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print("Incorrect password.")
        return

    # If the process reaches this point, the authentication was successful
    print("Authentication successful. You can continue with the program.")

# Example usage



is_available()

if not touch_id:
    touch_id_authenticate()
else:
    password_authenticate()

boot = False
def boot_sound_thread():
    global sound_done
    playsound('/Users/joshua.stanley/Desktop/   /pycoin/gen 2 (current)/startup.mp3')
    sound_done = True
if boot:   
    boot_thread = threading.Thread(target=boot_sound_thread)
    boot_thread.start()
    sound_done = False
    done = False
#here is the animation



#NO BOOTUP FOR THE TESTENV
if boot:
    print(Fore.YELLOW + "c")
    time.sleep(0.2)
    print(Fore.GREEN + "o")
    time.sleep(0.2)
    print("i")
    time.sleep(0.2)
    print("n")
    time.sleep(0.2)
    print("B")
    time.sleep(0.2)
    print("o")
    time.sleep(0.2)
    print("t")
    time.sleep(2)
    print(Fore.BLUE + "P")
    time.sleep(0.5)
    print("R")
    time.sleep(0.5)
    print("O")
    time.sleep(3.5)
    word = Fore.RED + "r e a l i z e  t h e  f u t u r e      "
    for letter in word:
        print(letter, end="", flush=True)
        time.sleep(0.01)



done = True

#Initializing the blockchain API


def get_ethereum_change():
    url = "https://api.coingecko.com/api/v3/coins/ethereum"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price_change_percentage_24h = data["market_data"]["price_change_percentage_24h"]
        return price_change_percentage_24h
    else:
        print("Failed to fetch change data. Status code:", response.status_code)
        return None

change = get_ethereum_change()


calls = 0
#this is a simple function to make calling in the API faster
def parse(url):
    #the 429 code checks if we exceeded our call limit, and waits if so
    
    
    global url_var, response, data
    url_var = url
    response = requests.get(url)
    data = json.loads(response.text)
    if response.status_code == 429:
        print(Fore.GREEN + 'Waiting...')
        while response.status_code == 429:
            time.sleep(5)
            #it will retry this command once done waitin
            url_var = url
            response = requests.get(url)
            data = json.loads(response.text)
    global api_fetch_number
    api_fetch_number = api_fetch_number + 1
    print(Fore.WHITE + 'API FETCH NUMBER: ' + Fore.BLUE + str(api_fetch_number))


parse('https://api.blockchain.com/v3/exchange/tickers/ETH-USD')
price = data['price_24h']
# Set the parameters for the API call

# Make the API call
parse('https://api.cryptowat.ch/markets/kraken/ethusd/ohlc')
interval = 60
ohlc_data = data['result'][str(interval)]
if response.status_code == 200:
    data = response.json()

    # Extract OHLC data from the response
    ohlc_data = data['result'][str(interval)]

    # Extract the lowest and highest prices
    
    lowest_price = min(candle[3] for candle in ohlc_data)
    highest_price = max(candle[2] for candle in ohlc_data)
else:
    print(f"Error {response.status_code}: Failed to fetch OHLC data")

api_online = False
#check if API is online
status_code = response.status_code
parse('https://api.coingecko.com/api/v3/ping')
if status_code == 200:
    #api is online
    api_online = True
else:
    print(Fore.RED + "One of our main API server's is down right now. Please try again later.")
    print('API Error code: ' + status_code)
    print('API: COIN_GECKO')




#INTITIALIZING YOUR METAMASK ACCOUNT



text_to_check = "private_key"  # Replace this with the text you want to check for
check_file_for_text(text_to_check)

# Connect to the Ethereum network using an Infura endpoint
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/c7e108cd8b3c4c4e83ff57734cddc77f'))
if not private_key:   
    private_key = input(Fore.BLUE + "Please input your private key.")
    write_encrypted_data_to_file('private_key')
    with open("/Users/joshua.stanley/Desktop/   /pycoin/gen 2 (current)/private_key.txt", "a") as file:
        file.write(private_key + "\n")
    print("Private Key Saved")


else:
    #check the other non created file for their key itself
    with open("/Users/joshua.stanley/Desktop/   /pycoin/gen 2 (current)/private_key.txt", "r") as file:
        
        first_line = file.readline().rstrip()  # Read the first line and remove trailing newline character ('\n')
        if first_line:
            private_key = first_line
            first_character = private_key[0]  # Retrieve the first character of the private key

            
            
        
            

# Example usage




url = 'https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=1&interval=30m'

response = requests.get(url)
data = response.json()

prices = data['prices']

# Get the latest 30-minute interval data point
latest_interval = prices[-1]
latest_price = latest_interval[1]

# Calculate high, low, open, and close from prices list
high_price = max(prices, key=lambda x: x[1])[1]
low_price = min(prices, key=lambda x: x[1])[1]
open_price = prices[0][1]
close_price = latest_price






Account = Account.from_key(private_key)
address = Account.address
web3.eth.defaultAccount = address   
my_account = Account.address
print(Fore.GREEN + "Loaded account:" + address)



# Get the current date and time
now = datetime.now()

# Set the time to the start of the day (midnight)
start_of_day = datetime(year=now.year, month=now.month, day=now.day, hour=0, minute=0, second=0)

# Convert the start of the day to Unix timestamp
unix_timestamp = int(start_of_day.timestamp())

print("Unix timestamp of the start of today's daily candle:", unix_timestamp)


# Set the parameters for the API request
url = "https://api.cryptowat.ch/markets/kraken/ethusd/ohlc"
parameters = {
    "periods": "3600",  # Time interval in seconds (1 hour)
    "after": unix_timestamp,  # Unix timestamp of the start time
}

# Send the API request
response = requests.get(url, params=parameters)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the OHLC data from the response
    data = response.json()["result"]["3600"]

    # Process the OHLC data
    for item in data:
        timestamp = item[0]
        open = item[1]
        high = item[2]
        low = item[3]
        close = item[4]

        # Do something with the OHLC data (print in this example)
        print(f"Timestamp: {timestamp}")
        print(f"Open: {open}")
        print(f"High: {high}")
        print(f"Low: {low}")
        print(f"Close: {close}")
        print("---")
else:
    print("Error occurred:", response.status_code)


usdc_amount = 0



def getBalance():
    balance = w3.eth.get_balance(w3.eth.default_account)
    print("Account balance:", w3.fromWei(balance, 'ether'), "ETH")
from web3 import Web3


# Connect to the Ethereum network
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))


profit = 0

transactions = []
sell_transactions = []
profit_sell = 0
profit_buy = 0
profit = 0

def get_profit():
    while True:    
        global profit_sell, profit_buy
        time.sleep(1)
        for item in transactions:
            profit_buy = item * price
        for item in sell_transactions:
            profit_sell = item * price
        profit = profit_sell - profit_buy

profit_thread = threading.Thread(target=get_profit)
profit_thread.start()


# Function to swap USDC for ETH
def purchaseETH(amount_in_usdc):
    global transaction
    #save profit
    transactions.append(amount_in_usdc)

# Function to swap ETH for USDC
def sellETH(amount_in_eth):
    global sell_transactions
    sell_transactions.append(amount_in_eth)
# Example usage
amount_usdc = 10000  # Amount of USDC to swap
amount_eth = web3.toWei(1, 'ether')  # Amount of ETH to swap










# Get date of yesterday



#Now intitialize the api for calling indicators for the alg
indicator_api = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjQ3NjE1NmQ0OThkNzVkYTM2N2M1YzQ5IiwiaWF0IjoxNjg1NDYwNzY5LCJleHAiOjMzMTg5OTI0NzY5fQ.OzQ1y6AvDIcBKGcbeZKdG89NZnF-xzNqjkf80cNbaaA'

def check_doji_candle(symbol):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/ohlc?vs_currency=usd&days=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        open_price, high_price, low_price = data[-1][1:-1]
        
        body_size = abs(open_price - data[-1][0])
        total_size = high_price - low_price
        upper_shadow = high_price - max(open_price, data[-1][0])
        lower_shadow = min(open_price, data[-1][0]) - low_price
        
        is_doji = body_size <= total_size * 0.1 and upper_shadow >= total_size * 0.7 and lower_shadow >= total_size * 0.7
        global doji_sell, doji_buy
        if is_doji:
            if open_price < data[-1][0]:
                doji_buy = True
                doji_sell = False
                return "Buy"
            else:
                doji_buy = False
                doji_sell = True
                return "Sell"
                
        else:
            doji_buy = False
            doji_sell= False
            return "No doji candle found"

    else:
        return "Failed to fetch data from CoinGecko API"

# Example usage
symbol = "ethereum"
decision = check_doji_candle(symbol)
print(f"Decision for {symbol}: {decision}")
#this function will call every alg we need, avg them, adn then use that to execute a trade

    
def clear_terminal():
    os.system('clear')
from datetime import datetime, timedelta

def get_date_from_days_ago(days_ago):
    global cg_date
    today = datetime.now()
    target_date = today - timedelta(days=days_ago)
    cg_date = target_date.strftime("%d-%m-%Y")
    return cg_date
#EVERYTHING FROM HERE UNTIL THE NEXT NOTE IS AN ALGORITHM DATA BASE.


print('Fetching database info from coingecko. This could take up to 20 minutes.')
#1 means buy, 100 means sell
sma_data = 0
#sma algorithm
days_ago = 0
#SMA- 50 DAY

print(Fore.BLUE + 'Loading API Data. This may take a while.')

print('Fetching 7 day SMA.')
for i in range(7):
    days_ago = days_ago + 1
    get_date_from_days_ago(days_ago)
    parse(f'https://api.coingecko.com/api/v3/coins/ethereum/history?date={str(cg_date)}&localization=false')
    temp_data = data['market_data']['current_price']['usd']
    sma_data = sma_data + temp_data

short_sma = sma_data / 50

repetitions = 0
print('Fetching 21 day SMA.')
for i in range(21):
    days_ago = days_ago + 1
    get_date_from_days_ago(days_ago)
    parse(f'https://api.coingecko.com/api/v3/coins/ethereum/history?date={str(cg_date)}&localization=false')
    temp_data = data['market_data']['current_price']['usd']
    sma_data = sma_data + temp_data
long_sma = sma_data / 200


print('Fetching volume.')

parse('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_market_cap=false&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=false&precision=3')
volume = data['ethereum']['usd_24h_vol']



volume_threshold = 42500




print('Fetching RSI data.')

rsi_list = ()
avg_gain = 0
avg_loss = 0
days = 1
for i in range(13):
    days = days + 1
    parse(f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days={days}&interval=hourly')
    temp_data = data['prices']
    rsi_list = list(temp_data)
    if rsi_list[0] < rsi_list[12]:
        #price rose
        avg_gain = avg_gain + (str(rsi_list[12]) - str(rsi_list[0]))
    else:
        #price_fell
        avg_loss_loss = avg_loss + (rsi_list[0] - rsi_list[12])
    rsi_list = ()
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1+rs))


rsi_green_threshold = 70
rsi_red_threshold = 30
#WE START OUT WITH 1000 DOLLARS FOR 'TESTS'


print("Fetching today's OHLC")




balance = 1000
#EMA

smoothing_factor = 1.2

EMA = ((price - short_sma) * smoothing_factor) + short_sma

previous_price = price
print('Short SMA: ' + str(short_sma))
print('Long SMA: ' + str(long_sma))
print('EMA: ' + str(EMA))

if short_sma > long_sma:
    sma_trend = 'up'
else:
    sma_trend = 'down'


def update_price():
    while True:
        parse('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_market_cap=false&include_24hr_vol=false&include_24hr_change=true&include_last_updated_at=false&precision=3')
        global price, day_change
        price = data['ethereum']['usd']
        day_change = data['ethereum']['usd_24h_change']
        time.sleep(60)
price_thread = threading.Thread(target=update_price)
price_thread.start()

print('Preprocessing finished. Bot starting.')


def two_hour_timer():
    global done
    done = False
    time.sleep(7200)
    done = True
two_hour_timer_thread = threading.Thread(target=two_hour_timer)
def ticker():
    print(price)
    print(change)
    #KEEP WRITING MORE
in_threshold = True
#always starts at 50, as it means to make no transactions at all
signal = 50
today = date.today()
#ranges from 1 - 10
breakout = True
#CHECK IF BREAKOUT COULD HAPPEN NOW
print(Fore.BLUE + 'Scanning for breakouts...')
if open < close:
    if high - close < 10:
        if close - open > 50:
            if volume > volume_threshold:
                if short_sma > long_sma:
                    #BREAKOUT CONDITIONS ARE FAVORABLE
                    #BUY ETHEREUM HERE
                    print('Supported Breakout Found. PURCHASING ETH.')
                    purchaseETH(balance / 20)
elif close - low < 10:
    if open - close > 50:
        if volume < volume_threshold:
            if long_sma < short_sma:
                #MARKET FALL CONDITIONS ARE FAVORABLE
                #SELL ETHEREUM HERE
                print('Supported market drop found. SELLING ETH.')
                sellETH(balance / 20)

else:
    print('No breakout found.')   
    breakout = False   

print('Scanning for market reversal patterns.')

rsi_multiplier = 0
saved_rsi = 0
if not breakout:
    if rsi > rsi_green_threshold:
        if volume < volume_threshold:
                print('Market Reversal Found!')

                rsi_multiplier = (rsi - 70) / 2
                saved_rsi = rsi
                print('Bot waiting until market begins falling.')
                while not saved_rsi - rsi > rsi_multiplier:
                    time.sleep(120)
                    rsi_list = ()
                    avg_gain = 0
                    avg_loss = 0
                    days = 1
                    for i in range(13):
                        days = days + 1
                        parse(f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days={days}&interval=hourly')
                        temp_data = data['prices']
                        rsi_list = list(temp_data)
                        if rsi_list[0] < rsi_list[12]:
                            #price rose
                            avg_gain = avg_gain + (rsi_list[12] - rsi_list[0])
                        else:
                            #price_fell
                            avg_loss_loss = avg_loss + (rsi_list[0] - rsi_list[12])
                        rsi_list = ()
                    rs = avg_gain / avg_loss
                    rsi = 100 - (100 / (1+rs))
                    sellETH(balance / 30)
elif rsi < rsi_red_threshold:
    if volume > volume_threshold:
        print('Market Reversal Found!')
        saved_rsi = rsi
        print('Bot waiting until market begins falling.')
        while not ((saved_rsi - rsi) / 2 ) + rsi > 30:
            time.sleep(120)
            rsi_list = ()
            avg_gain = 0
            avg_loss = 0
            days = 1
            for i in range(13):
                days = days + 1
                parse(f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days={days}&interval=hourly')
                temp_data = data['prices']
                rsi_list = list(temp_data)
                if rsi_list[0] < rsi_list[12]:
                    #price rose
                    avg_gain = avg_gain + (rsi_list[12] - rsi_list[0])
                else:
                    #price_fell
                    avg_loss_loss = avg_loss + (rsi_list[0] - rsi_list[12])
                    rsi_list = ()
                    rs = avg_gain / avg_loss
                    rsi = 100 - (100 / (1+rs))
        purchaseETH(balance / 30)
else:
    print('No market reversal found.')


#starting brakout strategy



url = 'https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=1&interval=30m'

response = requests.get(url)
data = response.json()

prices = data['prices']

# Get the latest 30-minute interval data point
latest_interval = prices[-1]
latest_price = latest_interval[1]

# Calculate high, low, open, and close from prices list
high_price = max(prices, key=lambda x: x[1])[1]
low_price = min(prices, key=lambda x: x[1])[1]
open_price = prices[0][1]
close_price = latest_price

print(high_price, low_price, open_price, close_price)







while True:
    time.sleep(10)
    if close_price - price < 5 and price - open_price > 15:
        if volume > volume_threshold:
            #BREAKOUTTTT
            purchaseETH(balance / 80)
    elif open_price - price > 15:
        if volume_threshold > volume_threshold:
            #BREAKOUTTT
            sellETH(balance / 80)
    else:
        print('Holding...')
    print(profit)




