from django.urls import include, path

from partneredu.users.views import (
    AnnouncementDetailView,
    AnnouncementListView,
    DashboardView,
    EventDetailView,
    EventListView,
    MapView,
    OrganizationDetailView,
    OrganizationListView,
    UserDetailView,
    UserRedirectView,
    UserUpdateView,
    join_event,
    join_organization,
    leave_event,
    leave_organization,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),
    path("~update/", view=UserUpdateView.as_view(), name="update"),
    path("users/<int:pk>/", view=UserDetailView.as_view(), name="detail"),
    path("dashboard", view=DashboardView.as_view(), name="dashboard"),
    path("events/", view=EventListView.as_view(), name="event_list"),
    path("events/<int:pk>/", view=EventDetailView.as_view(), name="event_detail"),
    path("organizations/", view=OrganizationListView.as_view(), name="organization_list"),
    path("organizations/<int:pk>/", view=OrganizationDetailView.as_view(), name="organization_detail"),
    path("recent/", view=AnnouncementListView.as_view(), name="announcement_list"),
    path("announcement/<slug:slug>/", view=AnnouncementDetailView.as_view(), name="announcement_detail"),
    path("map", view=MapView.as_view(), name="map"),
    path("event/join/<int:pk>/", view=join_event, name="event_join"),
    path("event/leave/<int:pk>/", view=leave_event, name="event_leave"),
    path("organization/subscribe/<int:pk>/", view=join_organization, name="organization_subscribe"),
    path("organization/unsubscribe/<int:pk>/", view=leave_organization, name="organization_unsubscribe"),
    path("api/", include("partneredu.users.api_views")),
]
