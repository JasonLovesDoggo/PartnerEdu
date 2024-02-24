from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import decorators, get_user_model
from django.utils.translation import gettext_lazy as _

from partneredu.users import models
from partneredu.users.forms import UserAdminChangeForm, UserAdminCreationForm

User: models.User = get_user_model()

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://docs.allauth.org/en/latest/common/admin.html#admin
    admin.site.login = decorators.login_required(admin.site.login)  # type: ignore[method-assign]


class StudentProfileInline(admin.StackedInline):
    max_num = 1  # only allow one student profile per user.
    model = models.StudentProfile
    can_delete = False
    fk_name = "user"
    verbose_name_plural = "student profile"


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["email", "name", "is_superuser"]
    search_fields = ["name"]
    ordering = ["id"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    inlines = [StudentProfileInline]


admin.site.site_header = "PartneredU Administration"
admin.site.register(models.Event)
admin.site.register(models.Organization)
admin.site.register(models.Announcement)
admin.site.register(models.Tag)
admin.site.register(models.Contact)
admin.site.register(models.Class)
admin.site.register(models.StudentProfile)
