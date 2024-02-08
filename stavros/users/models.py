from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models import CharField, EmailField, ManyToManyField, Model, TextField, CASCADE, ForeignKey
from django.forms import DateTimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from location_field.forms.plain import PlainLocationField

from stavros.users.managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for Stavros.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    subscribed_tags = ManyToManyField("Tag")
    subscribed_organizations = ManyToManyField("Organization")

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})


class Contact(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name="contacts")
    position = CharField(max_length=255)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",  # only allow proper phone numbers to be entered
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = CharField(validators=[phone_regex], max_length=17, blank=True)
    name = CharField(max_length=255)
    industry = CharField(max_length=255)
    event_type = CharField(max_length=255)
    resources = TextField()
    contacts = ManyToManyField("Contact")
    tags = ManyToManyField("Tag")


class Organization(Model):
    name = CharField(max_length=255)
    industry = CharField(max_length=255)
    event_type = CharField(max_length=255)
    resources = TextField()
    contacts = ManyToManyField("Contact")
    tags = ManyToManyField("Tag", related_name="organizations")


class Event(Model):
    name = CharField(max_length=255)
    info = TextField()
    start_date = DateTimeField()
    end_date = DateTimeField()
    organization = ForeignKey(Organization, on_delete=CASCADE, related_name="events")
    city = CharField(max_length=40)
    location = PlainLocationField(based_fields=["city"], zoom=7)
    tags = ManyToManyField("Tag", related_name="events")


class Tag(Model):
    name = CharField(max_length=255)
