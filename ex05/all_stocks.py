import sys


def all_stocks(string):
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
    string = string.replace(" ", '')
    companies = string.split(',')
    if '' in companies:
        return
    tickers = {value: key for key, value in COMPANIES.items()}
    for request in companies:
        ticker = request.upper()
        company = request.capitalize()
        if ticker in tickers:
            print(f'{ticker} is a ticker symbol for {tickers[ticker]}')
        elif company in COMPANIES:
            print(f'{company} stock price is {STOCKS[COMPANIES[company]]}')
        else:
            print(f'{request} is an unknown company or an unknown ticker symbol')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_stocks(sys.argv[1])