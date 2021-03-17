#import geopy
# pip install geopy
from functools import partial
from geopy.geocoders import Nominatim
from geopy import distance

#ZipCodez
FromZipCode = 90260
ShipTo = 'United States of America, Compton'


geolocator = Nominatim(user_agent="PO Automation Tool")
geocode = partial(geolocator.geocode, language="en")

from_location = geolocator.geocode(FromZipCode)
from_latitude= from_location.latitude
from_longitude = from_location.longitude
from_points = (from_latitude, from_longitude)

to_location = geolocator.geocode(ShipTo, addressdetails=True, language="en")
to_latitude= to_location.latitude
to_longitude = to_location.longitude
to_points = (to_latitude, to_longitude)

#print lat and long
print(from_latitude, ",",from_longitude)

#Returns Kilometers
distance_between = distance.distance(from_points, to_points)
print(distance_between)

#Returns Miles
distance_between_mi = distance.distance(from_points, to_points).miles
print(distance_between_mi, "mi")


#Function to append list to a dictionary
def add_list(dictionary, key, values):
    """Append al list to a single dictionay key"""
    if key not in dictionary:
        dictionary[key] = list()
    dictionary[key].extend(values)
    return dictionary


#Zip Code Loop
#loops through Zip code list and ads them to a dictionary with their ZipCode as the ID
zipcode_list = [90260, 90210, 90505, 99999]
zipcode_dict = {}
for i in zipcode_list:
    #print(i)
    location = geolocator.geocode(i)
    latitude= location.latitude
    longitude = location.longitude
    values = [latitude, longitude]
    zipcode_dict = add_list(zipcode_dict, i, values)

print(zipcode_dict)
