import os
from wget import download


class MapManager:
    def __init__(self, map_slots, download, debug, max_building_cost=9999999999999999999999):
        """
        Initializes the MapManager class
        :param map_slots: The number of map slots available
        :param download: Download new data
        :param debug: Run in debug mode
        :param max_building_cost: Maximum buliding cost (optional)
        """
        self.map_slots = map_slots
        self.download = download
        self.debug = debug
        self.buildings = None
        self.max_building_cost = max_building_cost

        self.prices = None

        self.exchange_file_name = 'exchange.csv'
        self.buildings_file_name = 'buildings.csv'
        self.products_file_name = 'products.csv'
        self.exchange_file_name = 'data/' + self.exchange_file_name
        self.buildings_file_name = 'data/' + self.buildings_file_name
        self.products_file_name = 'data/' + self.products_file_name

    def download_and_process(self):
        if self.download:
            print('Downloading data...')
            if self.exchange_file_name in os.listdir():  # Removes old versions of exchange_info.csv
                os.remove('exchange_info.csv')
            download('https://docs.google.com/spreadsheets/d/e/2PACX-1vTqF15cr_qWfAjNL-zp1IWH7RM_T-xudXewWO5IkNwpvBFYZHrglDFYs\
            dumH2EduNgysIFm2oB3g95n/pub?gid=1547132983&single=true&output=tsv', 'self.exchange_file_name')
            print('Exchange info downloaded')

            if self.buildings_file_name not in os.listdir():
                download('https://docs.google.com/spreadsheets/d/16J269YAFTVy_IPuzGUXfV_4-Rplzk1LVk7YpsvDcEVY/export?\
                format=tsv', 'self.buildings_file_name')
                print('Building info downloaded')
            else:
                print('Building info already downloaded')

            # TODO: Finish products.tsv and add download for it

        # I just read the csv manually, I couldn't figure out how to use pandas, and csv skipped the last week-ish.
        with open(self.exchange_file_name) as file:
            for _ in range(6):
                file.readline()
            names_list = file.readline().strip().split('\t')[3:]
            products_list = file.readline().strip().split('\t')[3:]

        # Creates a dict holding the prices of everything, using names_list and prices_list
        self.prices = {}
        for i in range(len(names_list)):
            self.prices[names_list[i]] = products_list[i]

        # TODO: Add processing for buildings.tsv into a list of str buildings and a dict of lists of info about them
        # TODO: Add processing for products.tsv into a dict of lists of info about them

    def run(self):
        pass
