from os import environ
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core import validators
from django.forms import CharField, EmailField, Field, MultipleChoiceField, forms
from django.utils.translation import gettext_lazy as _
from partneredu.users.models import Tag
from partneredu.users.utils.choices import ORGANIZATION_TYPES
User = get_user_model()


class MinLengthValidator(validators.MinLengthValidator):
    message = "Ensure this value has at least %(limit_value)d elements (it has %(show_value)d)."


class MaxLengthValidator(validators.MaxLengthValidator):
    message = "Ensure this value has at most %(limit_value)d elements (it has %(show_value)d)."


class CommaSeparatedCharField(Field):
    def __init__(self, dedup=True, max_length=None, min_length=None, *args, **kwargs):
        self.dedup, self.max_length, self.min_length = dedup, max_length, min_length
        super().__init__(*args, **kwargs)
        if min_length is not None:
            self.validators.append(MinLengthValidator(min_length))
        if max_length is not None:
            self.validators.append(MaxLengthValidator(max_length))

    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return []

        value = [item.strip() for item in value.split(",") if item.strip()]
        if self.dedup:
            value = list(set(value))

        return value

    def clean(self, value):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)
        return value


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        field_classes = {"email": EmailField}


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("email",)
        field_classes = {"email": EmailField}
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """

class EventSearchForm(forms.Form):
    name = CharField(label="Event Name", required=False)
    keywords = CharField(label="Keywords to search for", required=False)
    if environ.get("DJANGO_SETTINGS_MODULE") == "config.settings.test": # used so tests/compile messages works without db 
            tags = MultipleChoiceField(label="Tags to filter by", choices=[("example", "tag")], required=False)
    else:
        tags = MultipleChoiceField(label="Tags to filter by", choices=Tag.objects.values_list("name", "name"), required=False)

class OrganizationSearchForm(forms.Form):
    name = CharField(label="Organization Name", max_length=100, required=False)
    category = MultipleChoiceField(
        label="Organization type", choices=[(i, i) for i in ORGANIZATION_TYPES], required=False
    )
    keywords = CommaSeparatedCharField(label="Keywords", max_length=100, required=False)
    # if settings.DEBUG is False:
    #     location = PlainLocationField(label="Location", required=False)
    #     radius = FloatField(label="Radius (in km)", required=False, max_value=1000, min_value=0.1)
    # else:
    location = CharField(label="Location", required=False)

    def clean(self):
        # if settings.DEBUG is False:
        #     location = self.cleaned_data.get("location")
        #     radius = self.cleaned_data.get("radius")
        #     if location and not radius:
        #         raise ValidationError("Please provide a radius.")
        return self.cleaned_data
