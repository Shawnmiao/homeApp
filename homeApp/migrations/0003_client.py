# Generated by Django 4.2.4 on 2024-03-21 02:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("homeApp", "0002_branch"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("client_no", models.CharField(max_length=50, unique=True)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("tel_no", models.CharField(max_length=20)),
                ("street", models.CharField(max_length=30)),
                ("city", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=40)),
                ("pref_type", models.CharField(max_length=5)),
                ("max_rent", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
