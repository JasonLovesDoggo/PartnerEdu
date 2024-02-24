from django import template
from geopy.distance import geodesic

register = template.Library()


@register.simple_tag
def calculate_distance(user_latitude, user_longitude, event_latitude, event_longitude):
    user_location = (user_latitude, user_longitude)
    event_location = (event_latitude, event_longitude)
    return geodesic(
        user_location, event_location
    ).kilometers  # Return the distance in kilometers, change to .miles for miles
