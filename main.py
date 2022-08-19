import os
import wget

print('Welcome to the SimCo analyzer!')

# Downloads new prices
print('Downloading market price information...')
file_name = 'exchange_info.csv'
if file_name in os.listdir():  # Removes old versions of exchange_info.csv
    os.remove('exchange_info.csv')
wget.download('https://docs.google.com/spreadsheets/d/e/2PACX-1vTqF15cr_qWfAjNL-zp1IWH7RM_T-\
xudXewWO5IkNwpvBFYZHrglDFYsdumH2EduNgysIFm2oB3g95n/pub?gid=1547132983&single=true&output=csv', file_name)

# TODO: Figure out how to read csv. I keep getting charmap errors when I try.
