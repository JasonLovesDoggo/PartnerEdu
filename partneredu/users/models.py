from decimal import Decimal
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, RegexValidator
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    EmailField,
    ForeignKey,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
    AutoField,
)
from django.db.models.fields import DecimalField, IntegerField, PositiveIntegerField, URLField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from location_field.models.plain import PlainLocationField
from slugify.slugify import slugify

from partneredu.users.managers import UserManager
from partneredu.users.utils.choices import COURSE_OPTIONS, ORGANIZATION_TYPES, POSITIONS


class User(AbstractUser):
    """
    This is the User model. It represents a user in the system.
    It extends the AbstractUser model provided by Django.
    """

    # The name of the user. It can be blank.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    # The first name and last name fields are not used in this model.
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    # The email of the user. It must be unique.
    email = EmailField(_("email address"), unique=True)
    # The username field is not used in this model.
    username = None  # type: ignore

    # The email field is used as the username field.
    USERNAME_FIELD = "email"
    # There are no required fields.
    REQUIRED_FIELDS = []
    # The tags that the user is subscribed to.
    subscribed_tags = ManyToManyField("Tag")
    # The organizations that the user is subscribed to.
    subscribed_organizations = ManyToManyField("Organization", related_name="subscribers")
    # The contacts of the user.
    contacts = ManyToManyField("Contact", blank=True, related_name="contacts")
    # The manager for this model.
    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """
        This method returns the URL for the detail view of the user.
        """
        return reverse("users:detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        """
        This method returns the name of the user.
        """
        return self.name or self.email


class Class(Model):
    """
    This is the Class model. It represents a class in a school.
    """

    # The name of the class.
    name = CharField(max_length=255)
    # The subject of the class.
    subject = CharField(max_length=255, choices=COURSE_OPTIONS)
    # The grade level of the class.
    grade_level = IntegerField(choices=[(i, i) for i in range(9, 13)])
    # The teacher of the class.
    teacher = ForeignKey(User, on_delete=CASCADE, related_name="classes_teaching")
    # The students attending the class.
    students = ManyToManyField("StudentProfile", related_name="classes_attending", blank=True)

    def __str__(self) -> str:
        """
        This method returns the name of the class.
        """
        return f"{self.teacher.get_full_name()} - {self.name}"


class StudentProfile(Model):
    """
    This is the StudentProfile model. It represents a student's profile.
    """

    # The user associated with this profile.
    user = ForeignKey(User, on_delete=CASCADE, related_name="student_profile")
    # The birth date of the student.
    birth_date = DateTimeField()
    # The address of the student.
    address = PlainLocationField()
    # The year the student is graduating.
    graduating_year = CharField(max_length=255, choices=[(i, i) for i in range(2024, 2031)])
    # The unique ID of the student.
    student_id = CharField(unique=True, max_length=9)  # 9 digit student id
    # Any additional notes about the student.
    notes = TextField(blank=True, null=True)
    # The guidance counselor of the student.
    guidance_counselor = ForeignKey(User, on_delete=CASCADE, related_name="students", null=True, blank=True)
    # The classes that the student has taken.
    classes_taken = ManyToManyField("Class")
    # The contact information of the student's parents.
    parental_contact = ForeignKey("Contact", on_delete=CASCADE, related_name="children", null=True, blank=True)

    def __str__(self) -> str:
        """
        This method returns the name of the student.
        """
        return self.student_id


class Resource(Model):
    """
    This is the Resource model. It represents a resource.
    """

    # The title of the resource.
    title = CharField(max_length=255)
    # Any additional information about the resource.
    additional_info = TextField()
    # The link to the resource.
    link = URLField(null=True, blank=True)
    # The tags associated with the resource.
    tags = ManyToManyField("Tag", related_name="resources")

    def __str__(self) -> str:
        """
        This method returns the title of the resource.
        """
        return self.title


class Contact(Model):
    """
    This is the Contact model. It represents a contact.
    """

    # The internal name of the contact.
    internal_name = CharField(max_length=255)
    # The user associated with this contact.
    user = ForeignKey(User, on_delete=CASCADE, related_name="info")
    # The position of the contact in their company.
    company_position = CharField(max_length=255, blank=True, choices=POSITIONS)
    # The phone number of the contact.
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",  # only allow proper phone numbers to be entered
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    # Any additional notes about the contact.
    notes = TextField(blank=True, null=True)
    # The phone number of the contact.
    phone_number = CharField(validators=[phone_regex], max_length=17, blank=True)
    # The industry of the contact.
    industry = CharField(max_length=255, blank=True)
    # The tags associated with the contact.
    tags = ManyToManyField("Tag", blank=True, related_name="contacts")

    def __str__(self) -> str:
        """
        This method returns the internal name of the contact.
        """
        return self.user.get_full_name()


class Announcement(Model):
    """
    This is the Announcement model. It represents an announcement.
    """

    # The unique slug of the announcement.
    slug = SlugField(unique=True, editable=False, null=True, blank=True)
    # The title of the announcement.
    title = CharField(max_length=255)
    # The content of the announcement.
    content = TextField()
    # The date the announcement was posted.
    date_posted = DateTimeField(auto_now_add=True, editable=False)
    # The tags associated with the announcement.
    tags = ManyToManyField("Tag", related_name="announcements")
    # The organization that posted the announcement.
    organization = ForeignKey("Organization", on_delete=CASCADE, related_name="announcements")

    def save(self, *args, **kwargs):
        """
        This method is called when the announcement is saved.
        It generates a unique slug for the announcement.
        """
        if not self.id or not self.slug:  # only on creation
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """
        This method returns the title of the announcement.
        """
        return self.title


class Organization(Model):
    """
    This is the Organization model. It represents an organization.
    """
    id = AutoField(primary_key=True)
    # The name of the organization.
    name = CharField(max_length=200)
    # The category of the organization.
    category = CharField(max_length=255, choices=[(i, i) for i in ORGANIZATION_TYPES])
    # The resources associated with the organization.
    resources = ManyToManyField("Resource", related_name="organizations", blank=True)
    # The contacts associated with the organization.
    contacts = ManyToManyField("Contact", blank=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",  # only allow proper phone numbers to be entered
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    # The phone number of the organization.
    phone_number = CharField(validators=[phone_regex], max_length=17, blank=True)
    # The website of the organization.
    website = URLField(blank=True)
    # the email of the organization.
    email = EmailField(blank=True)
    # The tags associated with the organization.
    tags = ManyToManyField("Tag", related_name="organizations")
    # The description of the organization.
    description = TextField(max_length=500, blank=True, null=True)
    # The location of the organization's HQ.
    location = PlainLocationField()

    def __str__(self) -> str:
        """
        This method returns the name of the organization.
        """
        return self.name


class Event(Model):
    """
    This is the Event model. It represents an event.
    """

    # The name of the event.
    name = CharField(max_length=255)
    # Any additional information about the event.
    info = TextField()
    # The start date of the event.
    start_date = DateTimeField()
    # The end date of the event.
    end_date = DateTimeField()
    # The organization that is hosting the event.
    organization = ForeignKey(Organization, on_delete=CASCADE, related_name="events")
    # The location of the event.
    location = PlainLocationField()
    # The tags associated with the event.
    tags = ManyToManyField("Tag", related_name="events")
    # The users who are attending the event.
    attendees = ManyToManyField(User, related_name="events", blank=True)
    # The max amount of attendees for the event. If None, there is no limit.
    max_attendees = PositiveIntegerField(null=True, blank=True)
    # The price associated with the event. If None, the event is free.
    price = DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal("0"))], default=0.00)

    def __str__(self) -> str:
        """
        This method returns the name of the event.
        """
        return self.name


class Tag(Model):
    """
    This is the Tag model. It represents a tag.
    """

    # The name of the tag.
    name = CharField(max_length=255)

    def __str__(self) -> str:
        """
        This method returns the name of the tag.
        """
        return self.name
