from django.urls import path

from stavros.users.views import *

app_name = "users"
urlpatterns = [
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),
    path("~update/", view=UserUpdateView.as_view(), name="update"),
    path("users/<int:pk>/", view=UserDetailView.as_view(), name="detail"),
    path("", view=DashboardView.as_view(), name="dashboard"),
    path("events/", view=EventListView.as_view(), name="event_list"),
    path("events/<int:pk>/", view=EventDetailView.as_view(), name="event_detail"),
    path("organizations/", view=OrganizationListView.as_view(), name="organization_list"),
    path("organizations/<slug:slug>/", view=OrganizationDetailView.as_view(), name="organization_detail"),
    path("recent/", view=AnnouncementListView.as_view(), name="announcement_list"),
    path("announcement/<slug:slug>/", view=AnnouncementDetailView.as_view(), name="announcement_detail"),
    path("map", view=MapView.as_view(), name="map"),
]
