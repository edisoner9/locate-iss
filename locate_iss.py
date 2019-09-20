

# Edison Er
# 09/09/19

import requests, json

#----------------------------------------------------------------------------------------------------------#

# Current Location
location_now = 'http://api.open-notify.org/iss-now.json'
location_response = requests.get(location_now)

timestamp = location_response.json()['timestamp']
latitude = location_response.json()['iss_position']['latitude']
longitude = location_response.json()['iss_position']['longitude']

print("The current location of the ISS at timestamp %d is %s degrees latitude and %s degrees longitude.\n"
      % (timestamp, latitude, longitude))
 
#-------------------------------------------------------------------------#
    
# Passing Details

passing = 'http://api.open-notify.org/iss-pass.json?lat=45.0&lon=-122.3'
passing_response = requests.get(passing)

passing_latitude = passing_response.json()['request']['latitude']
passing_longitude = passing_response.json()['request']['longitude']
amount = passing_response.json()['request']['passes']


print("The ISS will pass over the location %f degrees latitude and %f degrees longitude %d times.\n"
      % (passing_latitude, passing_longitude, amount))

for num in range(amount):
    risetime = passing_response.json()['response'][num]['risetime']
    duration = passing_response.json()['response'][num]['duration']
    
    print("At risetime %d, it will pass for a duration of %d seconds." % (risetime, duration))

#----------------------------------------------------------------------------------------------------------#

# People in Space
people = 'http://api.open-notify.org/astros.json'
people_response = requests.get(people)
people_list = people_response.json()['people']

print("\nThere are", len(people_list), "people in space right now. They are:\n")


for num in range(len(people_response.json()['people'])):
    name = people_response.json()['people'][num]['name']
    craft = people_response.json()['people'][num]['craft']
    print("%s on the %s." % (name, craft))


