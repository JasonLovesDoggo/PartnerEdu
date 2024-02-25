import json

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Case, F, IntegerField, Q, When
from django.db.models.fields import DurationField
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

import partneredu
from partneredu.users.forms import OrganizationSearchForm
from partneredu.users.models import Announcement, Event, Organization

# if settings.DEBUG is False:
#     from django.contrib.gis.db.models.functions import Distance
#     from django.contrib.gis.geos import fromstr
#     from django.contrib.gis.measure import D

# Get the user model from Django's built-in user model
User = get_user_model()


class MessageDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        """
        This method handles the GET request.
        """
        if "msg" in request.session and request.session["msg"] is not None:
            if "msg_err" in request.session:
                del request.session["msg_err"]
                messages.warning(request, request.session["msg"])
            else:
                messages.success(request, request.session["msg"])
            del request.session["msg"]

        return super().get(request, *args, **kwargs)


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
    template_name = "events/list.html"  # The template used for this view is 'event_list.html'
    context_object_name = "events"  # The name of the variable to be used in the template context is 'events'
    paginate_by = 10  # The number of events displayed per page is 10

    def get_queryset(self):
        """
        This method returns the queryset to be used for the list view.
        """
        if self.request.GET.get("attendance", None) is not None:
            return Event.objects.all().order_by("-attendees__count")
        now = timezone.now()  # Get the current time
        queryset = (
            Event.objects.annotate(
                relevance=Case(
                    When(start_date__lte=now, end_date__gte=now, then=1),
                    When(start_date__gt=now, then=2),
                    When(end_date__lt=now, then=3),
                    output_field=IntegerField(),
                )
            )
            .annotate(
                timediff=Case(
                    When(start_date__gt=now, then=F("start_date") - now),
                    When(end_date__lt=now, then=now - F("end_date")),
                    default=0,
                    output_field=DurationField(),
                )
            )
            .order_by("relevance", "timediff")
        )
        return queryset  # Return the queryset


class EventDetailView(MessageDetailView):
    """
    This view is for displaying the details of an event.
    """

    model = Event  # The model being used is the Event model
    template_name = "events/detail.html"  # The template used for this view is 'event_detail.html'

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
    template_name = "organizations/list.html"  # The template used for this view is 'organization_list.html'
    context_object_name = (
        "organizations"  # The name of the variable to be used in the template context is 'organizations'
    )
    paginate_by = 10  # The number of organizations displayed per page is 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = OrganizationSearchForm()
        return context

    def get_queryset(self):
        form = OrganizationSearchForm(self.request.GET)
        object_list = self.model.objects.all().order_by("-subscribers")

        if form.is_valid():
            name = form.cleaned_data.get("name")
            category = form.cleaned_data.get("category")
            keywords = form.cleaned_data.get("keywords")
            location = form.cleaned_data.get("location")
            # radius = form.cleaned_data.get("radius")

            if name:
                object_list = object_list.filter(Q(name__icontains=name) | Q(description__icontains=name))

            if category:
                object_list = object_list.filter(category__in=category)
            if keywords:
                for keyword in keywords:
                    object_list = object_list.filter(description__icontains=keyword)
            if location:
                # if settings.DEBUG is False:
                #     lat, lon = location
                #     user_location = fromstr(f"POINT({lon} {lat})", srid=4326)
                #     object_list = object_list.annotate(distance=Distance("location", user_location)).filter(
                #         distance__lte=D(km=radius)
                #     )
                # else:
                object_list = object_list.filter(description__icontains=location)

        return object_list


class OrganizationDetailView(MessageDetailView):
    """
    This view is for displaying the details of an organization.
    """

    model = Organization  # The model being used is the Organization model
    template_name = "organizations/detail.html"  # The template used for this view is 'organization_detail.html'

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
    template_name = "announcements/list.html"  # The template used for this view is 'announcement_list.html'
    context_object_name = (
        "announcements"  # The name of the variable to be used in the template context is 'announcements'
    )
    paginate_by = 10  # The number of announcements displayed per page is 10

    def get_queryset(self):
        """
        This method returns the queryset to be used for the list view.
        """
        return Announcement.objects.filter(date_posted__lte=timezone.now()).order_by(
            "-date_posted"
        )  # Return all Announcement objects that were posted before the current time, \
        # ordered by date in descending order


class AnnouncementDetailView(DetailView):
    """
    This view is for displaying the details of an announcement.
    """

    model = Event  # The model being used is the Event model
    template_name = "announcements/detail.html"  # The template used for this view is 'announcement_detail.html'

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
        user: partneredu.users.models.User = request.user  # Get the currently logged in user
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


# Action views


def leave_event(request, pk):
    """
    This view is for allowing the user to leave an event.
    """
    event = get_object_or_404(Event, pk=pk)  # Get the event with the given primary key
    try:
        request.user.events.remove(event)  # Remove the user from the event
    except Exception:
        request.session["msg"] = "You are not in the event"
        request.session["msg_err"] = True
        return redirect("users:event_detail", pk=pk)
    # return a 200 to indicate success
    request.session["msg"] = "You left the event"
    return redirect("users:event_detail", pk=pk)


def join_event(request, pk):
    """
    This view is for allowing the user to join an event.
    """
    event = get_object_or_404(Event, pk=pk)  # Get the event with the given primary key
    if event.max_attendees is None or event.max_attendees > event.attendees.count():
        try:
            request.user.events.add(event)  # Add the user to the event
        except Exception:
            request.session["msg"] = "You are already in the event"
            request.session["msg_err"] = True
            return redirect("users:event_detail", pk=pk)
        # return a 200 to indicate success
        request.session["msg"] = "You joined the event"
        return redirect("users:event_detail", pk=pk)
    else:
        request.session["msg"] = "Event is full"
        return redirect("users:event_detail", pk=pk)


def leave_organization(request, pk):
    """
    This view is for allowing the user to leave an organization.
    """
    organization = get_object_or_404(Organization, pk=pk)  # Get the organization with the given primary key
    try:
        organization.subscribers.remove(request.user)  # Remove the user from the organization
    except Exception:
        request.session["msg"] = "You are not subscribed to the organization"
        request.session["msg_err"] = True
        return redirect("users:organization_detail", pk=pk)
    # return a 200 to indicate success
    request.session["msg"] = "You left the organization"
    return redirect("users:organization_detail", pk=pk)


def join_organization(request, pk):
    """
    This view is for allowing the user to join an organization.
    """
    organization = get_object_or_404(Organization, pk=pk)  # Get the organization with the given primary key
    try:
        organization.subscribers.add(request.user)  # Add the user to the organization
    except Exception:
        request.session["msg"] = f"You are already subscribed to {organization.name}"
        request.session["msg_err"] = True
        return redirect("users:organization_detail", pk=pk)
    # return a 200 to indicate success
    request.session["msg"] = "You joined the organization"
    return redirect("users:organization_detail", pk=pk)
