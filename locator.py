from geopy.geocoders import Nominatim

from geopy.distance import geodesic

import requests

def get_user_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data['loc'],split(',')
    except:
        print("Error: Unable to detect your location")
        return None, None
    
def find_nearby_places(lat, lon, place_type, radius):
    geolocator = Nominatim(user_agent="nearby_search")
    location = geolocator.reverse((lat, lon))
    print(f"\nYour current location: {location}\n")
    query = f"{place_type} near {lat}, {lon}"
    try:
        places = geolocator.geocode(query, exactly_one=False, limit=None)
        if places:
            for place in places:
                place_coords = (place.latitude, place.longitude)
                place_distance = geodesic((lat, lon), place_coords).kilometers
                if place_distance <= radius:
                    print(f"{place.address} ({place_distance:.2f} km)")
        else:
            print("No nearby places found for the given type")
    except:
        print("Error: Unable to fetch nearby places")

if __name__ == "__main__":
    user_lat, user_lon = get_user_location()
    if user_lat is not None and user_lon is not None:
        place_type = "hotels"
        search_radius = float(input("Radius"))
        find_nearby_places(float(user_lat), float(user_lon), place_type, search_radius)