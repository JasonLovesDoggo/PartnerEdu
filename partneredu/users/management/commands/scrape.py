from datetime import timedelta

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from partneredu.users.models import Event, Organization, Tag


class Command(BaseCommand):
    help = "Scraps the web for an event and adds it to the database"

    def add_arguments(self, parser):
        parser.add_argument("url_to_page", type=str, help="The URL to the page to scrape")

    def handle(self, *args, **options):
        if not options["url_to_page"]:
            raise CommandError("You must provide a URL to the page to scrape")

        url = options["url_to_page"]
        response = requests.get(url)
        if response.status_code != 200:
            raise CommandError(f"Failed to retrieve page: {url}")

        soup = BeautifulSoup(response.content, "html.parser")
        data = extract_data_from_html(soup, url)

        if Event.objects.filter(info=data["info"]).exists():
            self.stdout.write(self.style.WARNING(f"Event {data['name']} already exists in the database"))
            return

        org = Organization.objects.get(id=1)

        evnt = Event.objects.create(**data, organization=org)
        for tag in data["tags"]:
            tag_obj, _ = Tag.objects.get_or_create(name=tag)
            evnt.tags.add(tag_obj)
        evnt.save()
        self.stdout.write(self.style.SUCCESS(f"Successfully added {evnt} to the database from {url}"))


def extract_data_from_html(soup, url):
    name = soup.find("div", class_="box-content").find("a").text.strip()
    info = soup.find("div", class_="box-content").find("p").text.strip()

    data = {
        "name": name,
        "location": "43.667820,-79.394080",
        "organization": ["Royal Ontario Museum"],
        "price": 16.0,
        "start_date": timezone.now(),
        "end_date": timezone.now() + timedelta(minutes=60),
        "max_attendees": 35,
        "tags": ["Science", "Gallery", "Lesson", "Grades 1-12"],
        "info": info,
    }
    return data
