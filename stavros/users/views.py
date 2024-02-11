import json

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Case, F, IntegerField, When
from django.db.models.fields import DurationField
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

import stavros
from stavros.users.models import Announcement, Event, Organization

# Get the user model from Django's built-in user model
User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    """
    This view is for displaying the details of a user.
    It requires the user to be logged in to view their details.
    """

    model = User  # The model being used is the User model
    slug_field = "id"  # The field in the User model that's used for the lookup is 'id'
    slug_url_kwarg = "id"  # The name of the keyword argument in the URLconf is 'id'


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    This view is for updating the details of a user.
    It requires the user to be logged in to update their details.
    Upon successful update, a success message is displayed.
    """

    model = User  # The model being used is the User model
    fields = ["name"]  # The field that can be updated is 'name'
    success_message = _("Information successfully updated")  # The message displayed upon successful update

    def get_success_url(self):
        """
        This method returns the URL to redirect to after the user's details are successfully updated.
        """
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()  # The URL to redirect to is the user's detail view

    def get_object(self):
        """
        This method returns the User object to be updated.
        """
        return self.request.user  # The User object to be updated is the currently logged in user


class UserRedirectView(LoginRequiredMixin, RedirectView):
    """
    This view is for redirecting the user to their detail view.
    It requires the user to be logged in to be redirected.
    """

    permanent = False  # This is not a permanent redirect

    def get_redirect_url(self):
        """
        This method returns the URL to redirect to.
        """
        return reverse(
            "users:detail", kwargs={"pk": self.request.user.pk}
        )  # The URL to redirect to is the user's detail view


class EventListView(ListView):
    """
    This view is for displaying a list of events.
    """

    model = Event  # The model being used is the Event model
    template_name = "event_list.html"  # The template used for this view is 'event_list.html'
    context_object_name = "events"  # The name of the variable to be used in the template context is 'events'
    paginate_by = 10  # The number of events displayed per page is 10

    def get_queryset(self):
        """
        This method returns the queryset to be used for the list view.
        """
        now = timezone.now()  # Get the current time
        queryset = (
            Event.objects.annotate(
                relevance=Case(
                    When(date__gte=now, then=1),
                    When(date__lt=now, then=2),
                    output_field=IntegerField(),
                )
            )
            .annotate(
                timediff=Case(
                    When(date__gte=now, then=F("date") - now),
                    When(date__lt=now, then=now - F("date")),
                    output_field=DurationField(),
                )
            )
            .order_by("relevance", "timediff")
        )
        return queryset  # Return the queryset


class EventDetailView(DetailView):
    """
    This view is for displaying the details of an event.
    """

    model = Event  # The model being used is the Event model
    template_name = "event_detail.html"  # The template used for this view is 'event_detail.html'

    def get_object(self, queryset=None):
        """
        This method returns the Event object to be shown in detail view.
        """
        id_ = self.kwargs.get("pk")  # Get the primary key from the URL
        return get_object_or_404(Event, id=id_)  # Return the Event object with the given primary key


class OrganizationListView(ListView):
    """
    This view is for displaying a list of organizations.
    """

    model = Organization  # The model being used is the Organization model
    template_name = "organization_list.html"  # The template used for this view is 'organization_list.html'
    context_object_name = (
        "organizations"  # The name of the variable to be used in the template context is 'organizations'
    )
    paginate_by = 10  # The number of organizations displayed per page is 10

    def get_queryset(self):
        """
        This method returns the queryset to be used for the list view.
        """
        return Organization.objects.all()  # Return all Organization objects


class OrganizationDetailView(DetailView):
    """
    This view is for displaying the details of an organization.
    """

    model = Organization  # The model being used is the Organization model
    template_name = "organization_detail.html"  # The template used for this view is 'organization_detail.html'

    def get_object(self, queryset=None):
        """
        This method returns the Organization object to be shown in detail view.
        """
        slug_ = self.kwargs.get("slug")  # Get the slug from the URL
        return get_object_or_404(Organization, slug=slug_)  # Return the Organization object with the given slug


class AnnouncementListView(ListView):
    """
    This view is for displaying a list of announcements.
    """

    model = Event  # The model being used is the Event model
    template_name = "announcement_list.html"  # The template used for this view is 'announcement_list.html'
    context_object_name = (
        "announcements"  # The name of the variable to be used in the template context is 'announcements'
    )
    paginate_by = 10  # The number of announcements displayed per page is 10

    def get_queryset(self):
        """
        This method returns the queryset to be used for the list view.
        """
        return Announcement.objects.filter(date_posted__lte=timezone.now()).order_by(
            "-date"
        )  # Return all Announcement objects that were posted before the current time, \
        # ordered by date in descending order


class AnnouncementDetailView(DetailView):
    """
    This view is for displaying the details of an announcement.
    """

    model = Event  # The model being used is the Event model
    template_name = "announcement_detail.html"  # The template used for this view is 'announcement_detail.html'

    def get_object(self, queryset=None):
        """
        This method returns the Announcement object to be shown in detail view.
        """
        slug_ = self.kwargs.get("slug")  # Get the slug from the URL
        return get_object_or_404(Announcement, slug=slug_)  # Return the Announcement object with the given slug


class DashboardView(LoginRequiredMixin, View):
    """
    This view is for displaying the dashboard of the logged in user.
    It requires the user to be logged in to view their dashboard.
    """

    def get(self, request, *args, **kwargs):
        """
        This method handles the GET request.
        """
        user: stavros.users.models.User = request.user  # Get the currently logged in user
        context = {
            "user": user,  # The user to be displayed in the dashboard
            "events": user.events.all(),  # The events of the user
            "subscribed_orgs": user.subscribed_organizations.all(),  # The organizations that the user is subscribed to
            "followed_tags": user.subscribed_tags.all(),  # The tags that the user is following
        }
        return render(request, "dashboard.html", context)  # Render the dashboard with the given context


class MapView(View):
    """
    This view is for displaying a map with the locations of all organizations.
    """

    def get(self, request, *args, **kwargs):
        """
        This method handles the GET request.
        """
        locations = [
            [o.name, o.latitude, o.longitude, i] for i, o in enumerate(Organization.objects.all())
        ]  # Get the name, latitude, longitude, and index of all organizations
        context = {"locations": json.dumps(locations)}  # Convert the locations to JSON and add them to the context
        return render(request, "core/map_view.html", context)  # Render the map with the given context
