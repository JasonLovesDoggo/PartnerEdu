from django.http import JsonResponse
from django.urls import path
from django.views import View

from stavros.templatetags import calculate_distance


class DistanceView(View):
    """
    This view is for calculating the distance between the user's location and the event's location.
    """

    @staticmethod
    def get(request, *args, **kwargs):
        """
        This method handles the GET request.
        """
        user_latitude = request.GET.get("user_latitude")
        user_longitude = request.GET.get("user_longitude")
        event_latitude = request.GET.get("event_latitude")
        event_longitude = request.GET.get("event_longitude")

        distance = calculate_distance(user_latitude, user_longitude, event_latitude, event_longitude)

        return JsonResponse({"distance": distance})


urlpatterns = [
    path("distance/", DistanceView.as_view(), name="distance"),
]
