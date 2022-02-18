![](https://github.com/KateKo04/Twitter_application/blob/master/Blue%20and%20White%20Pop%20Etsy%20Banner.png)
# Explore a map of friends!

With the help of this application, you can find your(or someone else) friends' location.

## Interaction

To try this app out, go to http://kateko.pythonanywhere.com/.

Just type in the user, you want to have a map for and browse through it.

It can take some time for map to generate, so be patient about it.

![](https://github.com/KateKo04/Twitter_application/blob/master/twitter_birds.jpg)

In the example below, you can see location of Angela Merkel's friends.

On each marker you can see *screen_name* of friend.

![](https://github.com/KateKo04/Twitter_application/blob/master/map_merkel.jpg)

## Implementation

Files to connect to TwitterAPI: *twurl.py*, *oath.py*, *hidden.py*. 

Technologies used:
* Folium
* Flask (+html, css)
* Geopy
* Requests

To get .json information, file *twitter.py* is used. Here we extract "location" and "screen_name" of user.

Based on this information, with the help of *build_map.py* a map is constructed.

*web_app.py* stands for connecting all the .html files, that needed to display webapp for user.

In the directory *templates* there is a *home.html* file for user-friendly interaction.

In the directory *static* there are some style files for our *home.html*.
