import os
import wget


print('Welcome to the SimCo analyzer!')

# Downloads new prices
print('Downloading market price information...')
if 'exchange_info.csv' in os.listdir():
    print('exchange_info.csv in directory')
    os.remove('exchange_info.csv')
wget.download('https://docs.google.com/spreadsheets/d/e/2PACX-1vTqF15cr_qWfAjNL-zp1IWH7RM_T-\
xudXewWO5IkNwpvBFYZHrglDFYsdumH2EduNgysIFm2oB3g95n/pub?gid=1547132983&single=true&output=csv', 'exchange_info.csv')
