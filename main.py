import os
from wget import download

print('Welcome to the SimCo analyzer!')

exchange_file_name = 'exchange.csv'
buildings_file_name = 'buildings.csv'
products_file_name = 'products.csv'
debug = False
get_new_info = True

# Downloads info
if get_new_info:
    print('Downloading data...')

    if exchange_file_name in os.listdir():  # Removes old versions of exchange_info.csv
        os.remove('exchange_info.csv')
    download('https://docs.google.com/spreadsheets/d/e/2PACX-1vTqF15cr_qWfAjNL-zp1IWH7RM_T-xudXewWO5IkNwpvBFYZHrglDFYs\
    dumH2EduNgysIFm2oB3g95n/pub?gid=1547132983&single=true&output=tsv', exchange_file_name)
    print('Exchange info downloaded')
    download('https://docs.google.com/spreadsheets/d/16J269YAFTVy_IPuzGUXfV_4-Rplzk1LVk7YpsvDcEVY/export?format=tsv',
             buildings_file_name)
    print('Building info downloaded')

# I just read the csv manually, I couldn't figure out how to use pandas, and csv skipped the last week-ish.
with open(exchange_file_name) as file:
    for _ in range(6):
        file.readline()
    names_list = file.readline().strip().split('\t')[3:]
    prices_list = file.readline().strip().split('\t')[3:]

# Creates a dict holding the prices of everything, using names_list and prices_list
prices = {}
for i in range(len(names_list)):
    prices[names_list[i]] = prices_list[i]

if debug:
    print(prices)
