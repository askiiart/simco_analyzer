import os
import csv
import pickle

try:
    from wget import download
except ImportError as e:
    print('Error: Please install wget using "pip install wget"')
    exit(1)


class MapManager:
    def __init__(self, map_slots, max_building_cost=9999999999999999999999, **kwargs):
        """
        Initializes the MapManager class
        :param map_slots: The number of map slots available
        :param max_building_cost: Maximum building cost (optional)
        """
        self.map_slots = map_slots
        if 'download_new' in kwargs:
            self.download = kwargs['download_new']
        else:
            self.download = True
        if 'debug' in kwargs:
            self.debug = kwargs['debug']
        else:
            self.debug = False
        self.max_building_cost = max_building_cost

        self.prices = {}
        self.buildings = None
        self.products = None
        self.best_maps = None

        self.exchange_file_name = 'exchange.tsv'
        self.buildings_file_name = 'buildings.tsv'
        self.products_file_name = 'products.tsv'

        self.download_and_process()

    def download_and_process(self):
        # TODO: Simplify this logic
        # TODO: Add pickling for building and products info (not prices)

        if 'data' not in os.listdir():
            os.mkdir('data')
        os.chdir('data')
        if self.debug:
            print(os.listdir())

        # Exchange info download
        # This does not set the exchange info to not download, it is just a temporary bool to help with this logic.
        exchange_download = False
        if download:
            exchange_download = True
        elif self.exchange_file_name not in os.listdir():
            exchange_download = True

        if exchange_download:
            if self.exchange_file_name in os.listdir():
                os.remove(self.exchange_file_name)
            if self.debug:
                print('Downloading exchange info...')
            download(
                'https://docs.google.com/spreadsheets/d/e/2PACX-1vTqF15cr_qWfAjNL-zp1IWH7RM_T-xudXewWO5IkNwpvBFYZHrglDFYsdumH2EduNgysIFm2oB3g95n/pub?gid=1547132983&single=true&output=tsv',
                self.exchange_file_name)
            if self.debug:
                print('Exchange info downloaded')

        # Buildings download
        if f'{self.buildings_file_name[:-4]}.pickle' in os.listdir():
            pickle.load(open(f'{self.buildings_file_name[:-4]}.pickle', 'rb'))
        elif self.buildings_file_name not in os.listdir():
            if self.debug:
                print('Downloading building info...')
            download(
                'https://docs.google.com/spreadsheets/d/16J269YAFTVy_IPuzGUXfV_4-Rplzk1LVk7YpsvDcEVY/export?format=tsv',
                self.buildings_file_name)
            if self.debug:
                print('Building info downloaded')
        else:
            print('Building info already downloaded, but not pickled')

        # Products download
        if f'{self.products_file_name[:-4]}.pickle' in os.listdir():
            pickle.load(open(f'{self.products_file_name[:-4]}.pickle', 'rb'))
        elif self.products_file_name not in os.listdir():
            download(
                'https://docs.google.com/spreadsheets/d/16S_NxDa0XLeTftzDDogrXLr9TWND6XrgYqxvuQ1a5q8/export?format=tsv',
                self.products_file_name)
            print('Product info downloaded')
        else:
            print('Product info already downloaded, but not pickled')

        # Prices tsv processing
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

        # Buildings tsv processing
        with open(self.buildings_file_name) as file:
            reader = csv.reader(file, delimiter='\t')  # Changes delimiter to tab for .tsv files
            self.buildings = {}
            for row in reader:
                temp = list(row)
                self.buildings[temp[0].lower()] = [row[i].lower() for i in range(1, len(row))]
        pickle.dump(self.buildings, open(f'{self.buildings_file_name[:-4]}.pickle', 'wb'))

        # Products tsv processing
        # TODO: Check if there's more outliers (other than Aero research), and update code accordingly
        # Outliers, aside from name and transport units, will be dealt with in _analyze_profit
        with open(self.products_file_name) as file:
            reader = csv.reader(file, delimiter='\t')  # Changes delimiter to tab for .tsv files
            self.products = {}
            for row in reader:
                temp = list(row)
                if temp[0] != 'Product' and temp[0] != '':
                    self.products[temp[0].lower()] = [row[i].lower() for i in range(1, len(row))]
                    if self.debug:
                        print(f'{temp[0].lower()}:', self.products[temp[0].lower()])
        pickle.dump(self.products, open(f'{self.products_file_name[:-4]}.pickle', 'wb'))

        os.chdir('..')

    def run(self):

        self.best_maps = []  # In the format [[[products list], profit per 24h, construction cost], [{products set (2)},
        # profit per 24h (2), construction cost (2)]]
        current_map = []

        products_list = list(self.products.keys())

        # TODO: Fix creation of the iterations (not the right word but IDK) of the map
        for i in range(len(products_list)):
            current_map[0] = [products_list[i]]
            for j in range(self.map_slots):
                k = i + j + 1
                current_map[0].append(products_list[k])
                if self.debug:
                    print(current_map[0])

    def _analyze_profit(self, products):
        pass

    def _map_cost(self, products):
        pass

    def get_results(self):
        pass
