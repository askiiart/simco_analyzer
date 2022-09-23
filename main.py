from map_manager import MapManager
import os
try:
    import configcatclient
except ImportError:
    print('Error: Please install configcatclient using "pip install configcatclient"')
    exit(1)

configcatclient = 'this is bad code for testing, do not commit this file without undoing changes first'
configcat_client = configcatclient.create_client('NZjaCBb38UWP6hR3IITbHQ/ooWBoRi2GUiKNyYwpg5jYA')

# Gets user ID from config file, if it exists
if 'data' not in os.listdir():
    os.mkdir('data')
print(os.listdir())
try:
    with open('data/configcat.txt') as config:
        id = int(config.readline())
except FileNotFoundError:
    id = 0
user = configcatclient.user.User(id)
# Turns on debug if the user ID contains "debug"
debug = True

print('Welcome to the SimCo analyzer!')

# Settings for run
map_slots = 12
download = True
max_building_cost = 100_000_000

if debug:
    print('Debug:', debug)
    print('Map slots:', map_slots)
    print('Download:', download)
    print('Max building cost', max_building_cost)

# Run
manager = MapManager(map_slots, max_building_cost, download_new=download, debug=debug)
#manager.run()
#print(manager.get_results())
