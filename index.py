import pandas as pd


excel_files = ['BSE.xlsx', 'S&P500.xlsx','FTSE100.xlsx','SSE.xlsx','markets.xlsx']

csv_files = ['BSE.csv', 'S&P500.csv','FTSE100.csv','SSE.csv','markets.csv']




for excel_file, csv_file in zip(excel_files, csv_files):
    df = pd.read_excel(excel_file)
    df.to_csv(csv_file, index=False)



 






