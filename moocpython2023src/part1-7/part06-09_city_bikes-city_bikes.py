# tee ratkaisu tänne
# Write your solution here

def get_station_data(filename:str):
    station_data = {}
    with open(filename) as station:
        for data in station:
            data = data.split(";")
            if data[0] != "Longitude":
                station_data[data[3]] = (float(data[0]),float(data[1]))

    return station_data

def distance(stations: dict, station1: str, station2: str):
    import math
    longitude1 = stations[station1][0]
    latitude1 = stations[station1][1]

    longitude2 = stations[station2][0]
    latitude2 = stations[station2][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
   
    max_names = tuple
    max_distance = 0.00

    for station1 in stations:

        for station2 in stations:
            if station1 != station2:
                
                current_distance = distance(stations, station1, station2)
                if current_distance > max_distance:

                    max_distance = current_distance
                    max_names = (station1,station2)
    return max_names[0],max_names[1], max_distance


