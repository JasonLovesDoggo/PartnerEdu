import json

from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from stavros.templatetags import calculate_distance


@csrf_exempt
def distance_view(request, *args, **kwargs):
    """
    This method handles the POST request.
    """
    if request.method == "POST":
        # Load JSON data from the request body
        data = json.loads(request.body)
        try:
            user_latitude = float(data.get("user_latitude"))
            user_longitude = float(data.get("user_longitude"))
            event_latitude = float(data.get("event_latitude"))
            event_longitude = float(data.get("event_longitude"))
        except (TypeError, ValueError):
            return JsonResponse({"error": "Invalid data."}, status=400)

        distance = calculate_distance(user_latitude, user_longitude, event_latitude, event_longitude)

        return JsonResponse({"distance": distance})
    else:
        # Return an error response for other request methods
        return JsonResponse({"error": "Only POST requests are allowed."}, status=405)


urlpatterns = [
    path("distance/", distance_view, name="distance"),
]
