import folium
import phonenumbers
from phonenumbers import geocoder

from phoneNumber import number

key="f489c5e2b52a49269350e418b50f6b56"

jonNumber=phonenumbers.parse(number)
yourLocation=geocoder.description_for_number(jonNumber,"en")
print(yourLocation)

# get servive provider
from phonenumbers import carrier
service_number=carrier.name_for_number(jonNumber,"en")
print(service_number)

# get longitude and latitude
from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(key)
query=str(yourLocation)
results=geocoder.geocode(query)
# print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng],popup=yourLocation).add_to(myMap)

# save to html file
myMap.save("yourLocation.html")

print("finished")
fp = open('yourLocation.html', 'w')
fp.write('first line')
fp.close()



