# Generated by Django 4.1.7 on 2023-03-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0003_remove_driver_licence_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="driver",
            name="license_number",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
