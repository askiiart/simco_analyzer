from map_manager import MapManager

print('Welcome to the SimCo analyzer!')

map_slots = 10
download_new = False
debug = False

manager = MapManager(map_slots, debug, download_new, max_building_cost=10_000_000)
manager.run()
print(manager.get_results())
