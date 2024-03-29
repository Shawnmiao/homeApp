# Generated by Django 4.2.4 on 2024-03-18 04:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff",
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
                ("staffno", models.CharField(max_length=10, unique=True)),
                ("fname", models.CharField(max_length=100)),
                ("lname", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                ("branchno", models.CharField(max_length=10)),
                ("dob", models.DateField()),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("telephone", models.CharField(blank=True, max_length=15, null=True)),
                ("mobile", models.CharField(blank=True, max_length=15, null=True)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
