import curses
import yaml
import requests


class bonfida_api:
    """Class to enclose the bonfida serum api (ref: https://docs.bonfida.com/#introduction)"""

    def __init__(self):
        self.active_pair = "BTC/USDC"

    def get_all_pairs():
        url = "https://serum-api.bonfida.com/pairs
        pairs = requests.get(url)
        return all_pairs

    def get_recent_trades_by_market_name(marketName):
        url = f"https://serum-api.bonfida.com/trades/{marketName}"
        recent_trades = requests.get(url)
        return recent_trades

    def get_recent_trades_by_market_address(marketAddress):
        url = f"https://serum-api.bonfida.com/trades/address/{marketAddress}"
        recent_trades = requests.get(url)
        return recent_trades

    def get_all_recent_trades():
        url = "https://serum-api.bonfida.com/trades/all/recent"
        recent_trades = requests.get(url)
        return recent_trades

    def get_volueme(marketName):
        url = f"https://serum-api.bonfida.com/volumes/{marketName}"
        volume = requests.get(url)
        return volume

    def get_orderbook(marketName):
        url = f"https://serum-api.bonfida.com/orderbooks/{marketName}"
        orderbook = requests.get(url)
        return url

    def get_historical_prices(marketName, resolution, startTime, endTime, limit):
        url = f"https://serum-api.bonfida.com/candles/{marketName}?resolution={resolution}&startTime={startTime}&endTime={endTime}&limit={limit}"
        historical_prices = requests.get(url)
        return historical_prices

    # TODO websocket?


def serum(stdscr):

    #TODO, will have to have nodelay(True) for not waiting on get ch?

    return

if __name__ == "__main__":
    curses.wrapper(serum)
