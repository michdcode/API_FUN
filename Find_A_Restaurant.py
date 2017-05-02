from geocode import get_geocode_location
import json
import httplib2
from datetime import date

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = [os.environ'fs_client_id']
foursquare_client_secret = [os.environ'fs_client_secret']


def findARestaurant(meal_type, location):
    #1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    lat_long = get_geocode_location(location)
    lat = lat_long[0]
    lon = lat_long[1]
    print lat
    print lon
    #2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
    #HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    current_date = []
    today = date.today()
    current_date.append(today)
    date_str = str(current_date[0]).replace("-", "")
    print date_str
    meal_str = meal_type.replace(" ", "+")
    foursquare_url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=%s&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret, date_str, lat, lon, meal_str))
    h = httplib2.Http()
    response, content = h.request(foursquare_url, 'GET')
    foursquare_result = json.loads(content)
    print foursquare_result




    #3. Grab the first restaurant
    #4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
    #5. Grab the first image
    #6. If no image is available, insert default a image url
    #7. Return a dictionary containing the restaurant name, address, and image url


if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
findARestaurant("Gyros", "Sydney Australia")