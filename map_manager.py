import os
import csv
from wget import download


class MapManager:
    def __init__(self, map_slots, download, debug, max_building_cost=9999999999999999999999):
        """
        Initializes the MapManager class
        :param map_slots: The number of map slots available
        :param download: Download new data
        :param debug: Run in debug mode
        :param max_building_cost: Maximum building cost (optional)
        """
        self.map_slots = map_slots
        self.download = download
        self.debug = debug
        self.buildings = None
        self.max_building_cost = max_building_cost

        self.prices = {}

        self.exchange_file_name = 'exchange.tsv'
        self.buildings_file_name = 'buildings.tsv'
        self.products_file_name = 'products.tsv'

        self.download_and_process()

    def download_and_process(self):
        os.chdir('data')
        exchange_download = False
        if self.download:
            if self.exchange_file_name in os.listdir():  # Removes old versions of exchange_info.csv
                os.remove(self.exchange_file_name)
            exchange_download = True
        if self.exchange_file_name not in os.listdir():
            print('Exchange info not detected, must be downloaded')
            exchange_download = True
        if exchange_download:
            print('Downloading data...')
            download('https://docs.google.com/spreadsheets/d/e/2PACX-1vTqF15cr_qWfAjNL-zp1IWH7RM_T-xudXewWO5IkNwpvBFYZHrglDFYsdumH2EduNgysIFm2oB3g95n/pub?gid=1547132983&single=true&output=tsv', self.exchange_file_name)
            print('Exchange info downloaded')

        if self.buildings_file_name not in os.listdir():
            download('https://docs.google.com/spreadsheets/d/16J269YAFTVy_IPuzGUXfV_4-Rplzk1LVk7YpsvDcEVY/export?format=tsv', self.buildings_file_name)
            print('Building info downloaded')
        else:
            print('Building info already downloaded')

        # TODO: Finish products.tsv and add download for it (duplicate logic from buildings.tsv)

        # I just read the csv manually, I couldn't figure out how to use pandas, and csv skipped the last week-ish.
        with open(self.exchange_file_name) as file:
            for _ in range(6):
                file.readline()
            names_list = file.readline().lower().strip().split('\t')[3:]
            prices_list = file.readline().strip().split('\t')[3:]

        # Creates a dict holding the prices of everything, using names_list and prices_list
        self.prices = {}
        for i in range(len(names_list)):
            self.prices[names_list[i]] = prices_list[i]

        # TODO: Add processing for buildings.tsv into a list of str buildings and a dict of lists of info about them
        '''
        with open(self.buildings_file_name) as file:
            reader = csv.reader(file, delimiter='\t')  # Changes delimiter to tab for .tsv files
            for i in range(len(reader)):
                print(reader[i])

        # TODO: Add processing for products.tsv into a dict of lists of info about them

        os.chdir('..')
        '''

    def run(self):
        best_maps = []  # In the format [[[products list], profit per 24h, construction cost], [{products set (2)}, profit per 24h (2), construction cost (2)]]
        current_map = []
        current_map.append(list())

        # Loop through product names, then again adding
        for i in range(len(self.prices.keys())):
            for j in range(self.map_slots - 1):
                for k in range(len(self.prices.keys()):
                    k += 1 + j  # Offsets for starting position (1), and for already run loops



    def _analyze_profit(self):
        pass

    def get_results(self):
        pass
