from map_manager import MapManager

print('Welcome to the SimCo analyzer!')

map_slots = 12
download = True
debug = True
max_building_cost = 100_000_000

manager = MapManager(map_slots, max_building_cost, download_new=download, debug=debug)
#manager.run()
#print(manager.get_results())
