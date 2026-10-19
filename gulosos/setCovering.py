states_needed = set(["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"])

stations = {}
stations["98FM"] = set(["AL", "BA", "CE", "MA", "PE"])
stations["Caturite"] = set(["PB", "PI", "RN"])
stations["CBN"] = set(["AL", "BA", "CE", "MA", "PB"])
stations["Jovem Pan"] = set(["PE", "PI", "RN", "SE"])
stations["Rádio Educativa FM"] = set(["PE", "SE", "AL"])
stations["CNN"] = set(["BA", "CE", "MA"])

def my_set_covering(states_needed, stations):
    final_stations = set()
    while states_needed:
        states_covered = set()
        best_station = None
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered) and station not in final_stations:
                states_covered = covered
                best_station = station
        if best_station is not None:
            stations.pop(best_station)
            final_stations.add(best_station)
            states_needed -= states_covered
            print(f"Selected station: {best_station}, covers states: {states_covered}")
        else:
            return None
    return final_stations

print(my_set_covering(states_needed, stations))