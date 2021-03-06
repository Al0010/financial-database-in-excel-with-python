# Import libraries 
import pandas as pd
import pandas_datareader.data as web
import datetime as dt

# Make the dataframe visible on the shell
pd.set_option('display.max_rows',100000,'display.max_columns',100000)

# Set time periods
StartDate = dt.datetime(2021,1,1)
EndDate = dt.datetime(2022,3,10)

# Call data from Yahoo Finance
nasdaq = web.DataReader('^IXIC', 'yahoo', StartDate, EndDate)
facebook = web.DataReader('FB', 'yahoo', StartDate, EndDate)
netflix = web.DataReader('NFLX', 'yahoo', StartDate, EndDate)
amazon = web.DataReader('AMZN', 'yahoo', StartDate, EndDate)
google = web.DataReader('GOOGL', 'yahoo', StartDate, EndDate)
nvidia = web.DataReader('NVDA', 'yahoo', StartDate, EndDate)
tesla = web.DataReader('TSLA', 'yahoo', StartDate, EndDate)
nikola = web.DataReader('NKLA', 'yahoo', StartDate, EndDate)
ferrari = web.DataReader('RACE', 'yahoo', StartDate, EndDate)

# Delete dates from the index
nasdaq.reset_index(inplace = True)
facebook.reset_index(inplace = True)
netflix.reset_index(inplace = True)
amazon.reset_index(inplace = True)
google.reset_index(inplace = True)
nvidia.reset_index(inplace = True)
tesla.reset_index(inplace = True)
nikola.reset_index(inplace = True)
ferrari.reset_index(inplace = True)

# Extrapolates data 
open_nasdaq = nasdaq["Open"]
close_nasdaq = nasdaq["Close"]
open_facebook = facebook["Open"]
close_facebook = facebook["Close"]
open_netflix = netflix["Open"]
close_netflix = netflix["Close"]
open_amazon = amazon["Open"]
close_amazon = amazon["Close"]
open_google = google["Open"]
close_google = google["Close"]
open_nvidia = nvidia ["Open"]
close_nvidia = nvidia ["Close"]
open_tesla = tesla["Open"]
close_tesla = tesla["Close"]
open_nikola = nikola["Open"]
close_nikola = nikola["Close"]
open_ferrari = ferrari["Open"]
close_ferrari = ferrari["Close"]

# CREATE SHEET 1 
price = pd.DataFrame({
    'Date':nasdaq["Date"],
    'NasdaqOpen':open_nasdaq,
    'NasdaqClose':close_nasdaq,
    'FacebookOpen':open_facebook,
    'FacebookClose':close_facebook,
    'NetflixOpen':open_netflix,
    'NetflixClose':close_netflix,
    'AmazonOpen':open_amazon,
    'AmazonClose':close_amazon,
    'GoogleOpen':open_google,
    'GoogleClose':close_google,
    'NvidiaOpen':open_nvidia,
    'NvidiaClose':close_nvidia,
    'TeslaOpen':open_tesla,
    'TeslaClose':close_tesla,
    'NikolaOpen':open_nikola,
    'NikolaClose':close_nikola,
    'FerrariOpen':open_ferrari,
    'FerrariClose':close_ferrari,
})

# Create Excel sheet
# YOUR DIRECTORY EXAMPLE: /Users/utente/Desktop/Test.xlsx
price.to_excel(excel_writer = r'YOUR_DIRECTORY')

# Print data on the shell 
print(price)