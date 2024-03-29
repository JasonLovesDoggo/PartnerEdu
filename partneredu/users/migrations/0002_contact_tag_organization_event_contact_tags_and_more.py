# Generated by Django 4.2.10 on 2024-02-08 18:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("position", models.CharField(max_length=255)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("industry", models.CharField(max_length=255)),
                ("event_type", models.CharField(max_length=255)),
                ("resources", models.TextField()),
                ("contacts", models.ManyToManyField(to="users.contact")),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("industry", models.CharField(max_length=255)),
                ("event_type", models.CharField(max_length=255)),
                ("resources", models.TextField()),
                ("contacts", models.ManyToManyField(to="users.contact")),
                ("tags", models.ManyToManyField(related_name="organizations", to="users.tag")),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("info", models.TextField()),
                ("city", models.CharField(max_length=40)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="events", to="users.organization"
                    ),
                ),
                ("tags", models.ManyToManyField(related_name="events", to="users.tag")),
            ],
        ),
        migrations.AddField(
            model_name="contact",
            name="tags",
            field=models.ManyToManyField(to="users.tag"),
        ),
        migrations.AddField(
            model_name="contact",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="contacts", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="subscribed_organizations",
            field=models.ManyToManyField(to="users.organization"),
        ),
        migrations.AddField(
            model_name="user",
            name="subscribed_tags",
            field=models.ManyToManyField(to="users.tag"),
        ),
    ]
