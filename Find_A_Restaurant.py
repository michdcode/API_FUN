from geocode import get_geocode_location
import json
import httplib2
from datetime import date

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = os.environ['fs_client_id']
foursquare_client_secret = os.environ['fs_client_secret']


def findARestaurant(meal_type, location):
    #1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    lat_long = get_geocode_location(location)
    lat = lat_long[0]
    lon = lat_long[1]
    print lat
    print lon
    #2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
    #HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    #MD - rather than just using today's date, I wrote some code to determine today's date so this can be re-used
    current_date = []
    today = date.today()
    current_date.append(today)
    date_str = str(current_date[0]).replace("-", "")
    # print date_str - testing result
    meal_str = meal_type.replace(" ", "+")
    foursquare_url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=%s&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret, date_str, lat, lon, meal_str))
    h = httplib2.Http()
    response, content = h.request(foursquare_url, 'GET')
    foursquare_result = json.loads(content)
    #3. Grab the first restaurant
    if foursquare_result == "":
        print "no responses for that input"
    else:
        first_restaurant = foursquare_result['response']['venues'][0]
        print first_restaurant
        restaurant_name = (first_restaurant['name'])
        restaurant_address_lst = first_restaurant['location']['formattedAddress']
        # MTD - had to add exception handling because sometimes formattedAddress has only one item on list
        try:
            st_add, city_state_zip = restaurant_address_lst[0], restaurant_address_lst[1]
            restaurant_address = "%s, %s" % (st_add, city_state_zip)
        except IndexError:
            restaurant_address = restaurant_address_lst
        venue_id = first_restaurant['id']
        # MD - print venue_id - testing result
    #4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
        foursquare_photo_url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=%s&client_secret=%s' % (venue_id, foursquare_client_id, date_str, foursquare_client_secret))
        photo_URL_response, photo_URL_content = h.request(foursquare_photo_url, 'GET')
        photo_result = json.loads(photo_URL_content)
        photo_count = photo_result['response']['photos']['count']
        # MD - print photo_count - testing result
    #6. If no image is available, insert default a image url
        if photo_count == 0:
            photo_URL = "https://cdn.pixabay.com/photo/2014/09/13/21/30/dinner-table-444434_960_720.jpg"
    #5. Grab the first image
        else:
            photo = photo_result['response']['photos']['items'][0]
                photo_URL_prefix, photo_size, photo_URL_suffix = photo['prefix'], '300x300', photo['suffix']
                photo_URL = photo_URL_prefix + photo_size + photo_URL_suffix
    #7. Return a dictionary containing the restaurant name, address, and image url
        restaurant_results = {'name': restaurant_name, 'address': restaurant_address, 'image_url': photo_URL}
        print restaurant_results


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