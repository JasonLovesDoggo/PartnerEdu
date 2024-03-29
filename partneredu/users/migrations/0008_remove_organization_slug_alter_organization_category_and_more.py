# Generated by Django 4.2.10 on 2024-02-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_remove_organization_event_type_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organization",
            name="slug",
        ),
        migrations.AlterField(
            model_name="organization",
            name="category",
            field=models.CharField(
                choices=[
                    ("Software as a Service (SaaS) provider", "Software as a Service (SaaS) provider"),
                    ("Healthcare provider", "Healthcare provider"),
                    ("Fitness center", "Fitness center"),
                    ("Internet company", "Internet company"),
                    ("Government contractor", "Government contractor"),
                    ("Trade union", "Trade union"),
                    ("Professional association", "Professional association"),
                    ("Biotechnology company", "Biotechnology company"),
                    ("Food bank", "Food bank"),
                    ("Art gallery", "Art gallery"),
                    ("Charity", "Charity"),
                    ("Arts organization", "Arts organization"),
                    ("Event management company", "Event management company"),
                    ("Professional sports league", "Professional sports league"),
                    ("Social service agency", "Social service agency"),
                    ("Music venue", "Music venue"),
                    ("Tutoring service", "Tutoring service"),
                    ("Educational institution", "Educational institution"),
                    ("Public policy institute", "Public policy institute"),
                    ("Advertising agency", "Advertising agency"),
                    ("Technology company", "Technology company"),
                    ("Pharmaceutical company", "Pharmaceutical company"),
                    ("Cybersecurity firm", "Cybersecurity firm"),
                    ("Research institute", "Research institute"),
                    ("Automobile manufacturer", "Automobile manufacturer"),
                    ("Government agency", "Government agency"),
                    ("Dental clinic", "Dental clinic"),
                    ("Military organization", "Military organization"),
                    ("Cloud computing company", "Cloud computing company"),
                    ("Labor union", "Labor union"),
                    ("Brokerage firm", "Brokerage firm"),
                    ("Aerospace company", "Aerospace company"),
                    ("Career counseling center", "Career counseling center"),
                    ("Fitness equipment manufacturer", "Fitness equipment manufacturer"),
                    ("Real estate agency", "Real estate agency"),
                    ("Film studio", "Film studio"),
                    ("Talent agency", "Talent agency"),
                    ("Construction company", "Construction company"),
                    ("Bank", "Bank"),
                    ("Retail chain", "Retail chain"),
                    ("Food delivery service", "Food delivery service"),
                    ("Financial institution", "Financial institution"),
                    ("Credit union", "Credit union"),
                    ("Venture capital firm", "Venture capital firm"),
                    ("Shipping company", "Shipping company"),
                    ("Fine arts school", "Fine arts school"),
                    ("Nonprofit organization", "Nonprofit organization"),
                    ("Consumer goods company", "Consumer goods company"),
                    ("Think tank", "Think tank"),
                    ("Language school", "Language school"),
                    ("Investment firm", "Investment firm"),
                    ("Cultural center", "Cultural center"),
                    ("Hedge fund", "Hedge fund"),
                    ("Medical device manufacturer", "Medical device manufacturer"),
                    ("Museum", "Museum"),
                    ("Law firm", "Law firm"),
                    ("Library", "Library"),
                    ("School", "School"),
                    ("Youth organization", "Youth organization"),
                    ("Human resources agency", "Human resources agency"),
                    ("Private equity firm", "Private equity firm"),
                    ("Community center", "Community center"),
                    ("Tourism board", "Tourism board"),
                    ("University", "University"),
                    ("Pharmaceutical laboratory", "Pharmaceutical laboratory"),
                    ("Performing arts school", "Performing arts school"),
                    ("Tour operator", "Tour operator"),
                    ("Energy company", "Energy company"),
                    ("Software development firm", "Software development firm"),
                    ("Gaming company", "Gaming company"),
                    ("Healthcare consultancy", "Healthcare consultancy"),
                    ("Marketing agency", "Marketing agency"),
                    ("Healthcare system", "Healthcare system"),
                    ("Manufacturing company", "Manufacturing company"),
                    ("Environmental organization", "Environmental organization"),
                    ("Telecommunications company", "Telecommunications company"),
                    ("Transportation company", "Transportation company"),
                    ("Public relations firm", "Public relations firm"),
                    ("Social club", "Social club"),
                    ("Amusement park", "Amusement park"),
                    ("Logistics company", "Logistics company"),
                    ("Animation studio", "Animation studio"),
                    ("Online learning platform", "Online learning platform"),
                    ("Streaming service", "Streaming service"),
                    ("Volunteer organization", "Volunteer organization"),
                    ("Beverage company", "Beverage company"),
                    ("Retail store", "Retail store"),
                    ("Medical clinic", "Medical clinic"),
                    ("Laboratory", "Laboratory"),
                    ("Travel agency", "Travel agency"),
                    ("Professional society", "Professional society"),
                    ("Chamber of commerce", "Chamber of commerce"),
                    ("Social media platform", "Social media platform"),
                    ("Web hosting company", "Web hosting company"),
                    ("Legal consultancy", "Legal consultancy"),
                    ("Hospitality company", "Hospitality company"),
                    ("Wealth management firm", "Wealth management firm"),
                    ("Fashion brand", "Fashion brand"),
                    ("Television network", "Television network"),
                    ("Media company", "Media company"),
                    ("Trade association", "Trade association"),
                    ("Test prep company", "Test prep company"),
                    ("Corporation", "Corporation"),
                    ("Franchise", "Franchise"),
                    ("Startup", "Startup"),
                    ("E-commerce platform", "E-commerce platform"),
                    ("Political party", "Political party"),
                    ("Animal shelter", "Animal shelter"),
                    ("Athletic apparel brand", "Athletic apparel brand"),
                    ("Restaurant", "Restaurant"),
                    ("Video game developer", "Video game developer"),
                    ("Sports team", "Sports team"),
                    ("College", "College"),
                    ("Financial advisory firm", "Financial advisory firm"),
                    ("Religious institution", "Religious institution"),
                    ("Software company", "Software company"),
                    ("Senior center", "Senior center"),
                    ("Cooperative", "Cooperative"),
                    ("Consulting firm", "Consulting firm"),
                    ("Legal aid organization", "Legal aid organization"),
                    ("Hotel", "Hotel"),
                    ("Hospital", "Hospital"),
                    ("Foundation", "Foundation"),
                    ("Insurance company", "Insurance company"),
                    ("Theater", "Theater"),
                    ("Domain registrar", "Domain registrar"),
                    ("Artificial intelligence company", "Artificial intelligence company"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="subscribed_organizations",
            field=models.ManyToManyField(related_name="subscribers", to="users.organization"),
        ),
    ]
