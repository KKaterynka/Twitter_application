import folium
import twitter
import os
import json
import folium
import geopy
from geopy.geocoders import Nominatim

def total_info(usermn):
    """
    Function to extract information.
    """
    user_acc = twitter.get_user_location(usermn)
    # print(user_acc)

    map = folium.Map(tiles="Stamen Terrain", location=[40.7127281, -74.0060152], zoom_start=3)
    tooltip = 'Click For More Info'

    def exact_location(location):
        """
        Returns accurate location
        of the given inaccurate location.
                Parameters:
                        location (str): given (inaccurate) location
                Returns:
                        distance (str): accurate location
        >>> exact_location("Los Angeles, California, USA")
        Location(Los Angeles, Los Angeles County, California, United States, (34.0536909, -118.242766, 0.0))
        >>> exact_location("Coventry, West Midlands, England, UK")
        Location(Coventry, West Midlands Combined Authority, West Midlands, England, United Kingdom, (52.4081812, -1.510477, 0.0))
        """
        geo_address = Nominatim(user_agent='accurate-coordinates').geocode(location)
        return geo_address


    def create_map():
        """
        Function that creates a map for user.
        """
        f_markers = []
        for user in user_acc:
            user_loc_exact = exact_location(user[0])
            f_markers.append((user_loc_exact, user[1]))
        # print(f_markers)

        for i in range(0, len(f_markers)):

            try:
                if f_markers[i][0][1][0]:
                    folium.Marker(
                        location=[f_markers[i][0][1][0], f_markers[i][0][1][1]], tooltip=tooltip,
                        popup=f_markers[i][-1], icon=folium.Icon(color='cadetblue')
                    ).add_to(map)
            except:
                continue
    create_map()

    map.save(f'templates/{usermn}.html')