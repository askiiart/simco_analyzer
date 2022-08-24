import os
import wget

print('Welcome to the SimCo analyzer!')

file_name = 'exchange_info.csv'
debug = False
download = True

# Downloads new prices
if download:
    print('Downloading market price information...')
    if file_name in os.listdir():  # Removes old versions of exchange_info.csv
        os.remove('exchange_info.csv')
    wget.download('https://docs.google.com/spreadsheets/d/e/2PACX-1vTqF15cr_qWfAjNL-zp1IWH7RM_T-\
    xudXewWO5IkNwpvBFYZHrglDFYsdumH2EduNgysIFm2oB3g95n/pub?gid=1547132983&single=true&output=csv', file_name)
    print('Download finished!')

# I just read the csv manually, I couldn't figure out how to use pandas, and csv skipped the last week-ish.
with open(file_name) as file:
    for _ in range(6):
        file.readline()
    names_list = file.readline().strip().split(',')[3:]
    prices_list = file.readline().strip().split(',')[3:]

# Creates a dict holding the prices of everything, using names_list and prices_list
prices = {}
for i in range(len(names_list)):
    prices[names_list[i]] = prices_list[i]

if debug:
    print(prices)
