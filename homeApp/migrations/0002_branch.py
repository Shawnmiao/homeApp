# Generated by Django 4.2.4 on 2024-03-20 22:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("homeApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "branch_no",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("street", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=50)),
                ("postcode", models.CharField(max_length=10)),
            ],
        ),
    ]
