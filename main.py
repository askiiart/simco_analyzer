from map_manager import MapManager
try:
    import configcatclient
except ImportError:
    print('Error: Please install configcatclient using "pip install configcatclient"')
    exit(1)

configcat_client = configcatclient.create_client('NZjaCBb38UWP6hR3IITbHQ/ooWBoRi2GUiKNyYwpg5jYA')
with open('data/configcat.txt') as config:
    user = configcatclient.user.User(config.readline())  # Put the user id here

print('Welcome to the SimCo analyzer!')

map_slots = 12
download = True
# Turns on debug if the user ID contains "debug"
debug = configcat_client.get_value('debug', False, user)
print(debug)
max_building_cost = 100_000_000

#manager = MapManager(map_slots, max_building_cost, download_new=download, debug=debug)
#manager.run()
#print(manager.get_results())
