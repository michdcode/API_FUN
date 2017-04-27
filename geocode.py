# Exercise for Udacity Class "Designing Restful API's" 
import httplib2
import json


def get_geocode_location(input_string):
    "Get latitude & longitude of a city."

    google_api_key = os.environ['google_api_key']
    location_string = input_string.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (location_string,
                                                                                   google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
#   print result header to check data
    print ("response header: %s \n \n")% response
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)
# 32.715738, -117.1610838 (lat/long for San Diego, CA)

