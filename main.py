from map_manager import MapManager
import os

debug = True

print('Welcome to the SimCo analyzer!')

# Settings for run
map_slots = 12
download = True
max_building_cost = 100_000_000

# Turns on debug if the user ID contains "debug"
debug = configcat_client.get_value('debug', False, user)
if debug:
    print('Debug:', debug)
    print('Map slots:', map_slots)
    print('Download:', download)
    print('Max building cost', max_building_cost)

manager = MapManager(map_slots, max_building_cost, download_new=download, debug=debug)
#manager.run()
#print(manager.get_results())
