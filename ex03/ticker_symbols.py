import sys


def ticker_simbols(ticker):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    tickers = {value: key for key, value in COMPANIES.items()}
    if ticker in tickers:
        print(f'{tickers[ticker]} {STOCKS[ticker]}')
    else:
        print('Unknown company')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ticker_simbols(sys.argv[1].upper())