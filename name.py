import yfinance as yf

def symbol(ticker):
    msft = yf.Ticker(ticker)

    company_name = msft.info['longName']
    company_name_1=company_name.split()
    return company_name_1[0],ticker,company_name
