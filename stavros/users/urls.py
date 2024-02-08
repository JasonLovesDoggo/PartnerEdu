from django.urls import include, path

from stavros.users.views import UserDetailView, UserRedirectView, UserUpdateView
app_name = "users"
urlpatterns = [
    path("", include("pwa.urls")),
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),
    path("~update/", view=UserUpdateView.as_view(), name="update"),
    path("<int:pk>/", view=UserDetailView.as_view(), name="detail"),
    path("", include("django.contrib.flatpages.urls")),
]
