from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import IntegerField, When, F, Case
from django.db.models.fields import DurationField
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView
from django.shortcuts import get_object_or_404
from stavros.users.models import Event, Organization, Announcement

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})


class EventListView(ListView):
    model = Event
    template_name = "event_list.html"
    context_object_name = "events"
    paginate_by = 10

    def get_queryset(self):
        now = timezone.now()
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
        return queryset



class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Event, id=id_)


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "organization_detail.html"

    def get_object(self, queryset=None):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Organization, slug=slug_)

class AnnouncementListView(ListView):
    model = Event
    template_name = "announcement_list.html"
    context_object_name = "announcements"
    paginate_by = 10

    def get_queryset(self):
        return Announcement.objects.filter(date_posted__lte=timezone.now()).order_by('-date')

class AnnouncementDetailView(DetailView):
    model = Event
    template_name = "announcement_detail.html"

    def get_object(self, queryset=None):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Announcement, slug=slug_)
