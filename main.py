import pandas as pd
import yfinance as yf
from datetime import datetime

ticker = ["^GSPC","^BSESN","^FTSE","000001.SS"]
country = ["USA","IND","UK","CHN"]
index_name=["S&P 500","S&P BSE SENSEX","FTSE 100","SSE Composite Index"]

rows=[]

data = pd.DataFrame(columns=["country","Index_name","Year","Volume","Annual_returns","CAGR"])

end_date= datetime.now()
start_date= end_date.replace(year=end_date.year-10)

def calculate_cagr(start, end , periods):
    return (end/start)** (1/periods)-1

for ticker , country, index_name in zip(ticker , country, index_name):
    stock = yf.Ticker(ticker)
    hist= stock.history(start= start_date, end=end_date)
    hist.index = pd.to_datetime(hist.index)
    hist["Year"]=hist.index.year
    annual_data = hist['Close'].resample('Y').last()

    annual_returns = annual_data.pct_change() * 100
    annual_returns = annual_returns.dropna()
    annual_volume = hist['Volume'].resample('Y').sum()
   
    


    start = annual_data.iloc[0]
    end = annual_data[-1]
    periods = len(annual_data)-1

    CAGR = calculate_cagr(start , end , periods)*100
    

    for year in annual_data.index.year :
        rows.append({

         "country":country,
         "Index_name":index_name,
         "Year": year,
         "Volume": annual_volume.loc[annual_volume.index.year == year].values[0],
         "Annual_returns": annual_returns.loc[annual_returns.index.year == year].values[0] if year in annual_returns.index.year else None,
         "CAGR ":CAGR  if year == annual_data.index.year[-1] else None



        })

data = pd.DataFrame(rows)

data.to_csv("index_data.csv" , index= False)
   

    
