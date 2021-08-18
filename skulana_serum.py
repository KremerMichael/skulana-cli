import curses
import datetime
import time
import yaml
import requests

class wallet:
    """Class to enclose a solana wallet"""

class bonfida_api:
    """Class to enclose the bonfida serum api (ref: https://docs.bonfida.com/#introduction)"""

    def __init__(self):
        self.marketName = "BTCUSDC"

    def get_all_pairs(self) -> dict:
        url = "https://serum-api.bonfida.com/pairs"
        pairs = requests.get(url)
        return all_pairs.json()['data']

    def get_recent_trades_by_market_name(self) -> dict:
        url = f"https://serum-api.bonfida.com/trades/{self.marketName}"
        recent_trades = requests.get(url)
        return recent_trades.json()['data']

    def get_recent_trades_by_market_address(self, marketAddress) -> dict:
        url = f"https://serum-api.bonfida.com/trades/address/{marketAddress}"
        recent_trades = requests.get(url)
        return recent_trades.json()['data']

    def get_all_recent_trades(self) -> dict:
        url = "https://serum-api.bonfida.com/trades/all/recent"
        recent_trades = requests.get(url)
        return recent_trades.json()['data']

    def get_volueme(self) -> dict:
        url = f"https://serum-api.bonfida.com/volumes/{self.marketName}"
        volume = requests.get(url)
        return volume.json()['data']

    def get_orderbook(self) -> dict:
        url = f"https://serum-api.bonfida.com/orderbooks/{self.marketName}"
        orderbook = requests.get(url)
        return orderbook.json()['data']

    def get_historical_prices(self, resolution, startTime, endTime, limit) -> dict:
        url = f"https://serum-api.bonfida.com/candles/{self.marketName}?resolution={resolution}&startTime={startTime}&endTime={endTime}&limit={limit}"
        historical_prices = requests.get(url)
        return historical_prices.json()['data']

    # TODO websocket?
def run_command(command: str) -> bool:
    if command == "exit" or command == "q":
        return False
    else:
        return True

def serum(stdscr) -> None:

    # Initalize bonfida API
    bonfidaAPI = bonfida_api()

    #TODO, will have to have nodelay(True) for not waiting on get ch?
    stdscr.nodelay(True) # TODO this is slowwww

    # Setup colors
    curses.start_color()

    # Main loop
    command = ""
    running = True
    while running:

        # Get order book
        #time.sleep()
        orderbook = bonfidaAPI.get_orderbook()
        market_name = orderbook['market']
        bids = orderbook['bids']
        asks = orderbook['asks']

        # Get screen size
        screen_height, screen_width = stdscr.getmaxyx()

        # Write maket name

        # Get order book framming
        ask_start = 3
        ask_end = screen_height//2 - 1

        bid_start = screen_height//2 + 1
        bid_end = screen_height - 3

        # Print screen
        stdscr.clear()

        # Title
        stdscr.addstr(1, screen_width//2 - len(market_name)//2, market_name)

        # Orderbook
        delta = 0
        asks_len = len(asks)
        for i in range(ask_end, ask_start, -1):
            stdscr.addstr(i, 2, f"price {asks[delta]['price']} size {asks[delta]['size']}")
            delta+=1

        for i in range(bid_start, bid_end):
            stdscr.addstr(i, 2, f"price {bids[i]['price']} size {bids[i]['size']}")

        # print time
        _now = datetime.datetime.now()
        stdscr.addstr(1, 2, f"TIME: {_now.hour}:{_now.minute}:{_now.second}.{_now.microsecond}")

        # print wallet
        wallet_str = "WALLET: abc"
        stdscr.addstr(1, screen_width - len(wallet_str) - 1, wallet_str)


        # Set command window
        key = stdscr.getch() #TODO slow?
        if key == -1: # No input
            command = command
        elif key == curses.KEY_BACKSPACE or key in [8, 127]: # Backspace
            command = command[:-1]
        elif key == curses.KEY_ENTER or key in [10, 13]: # Enter
            running = run_command(command)
            command = ""
        else: # Anything else
            command += chr(key)
        prompt = f"skulana> {command}"
        stdscr.addstr(screen_height -1, 2, prompt)

        # Refresh new screen
        stdscr.refresh()


    return

if __name__ == "__main__":
    curses.wrapper(serum)
