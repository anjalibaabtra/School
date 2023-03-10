# Generated by Django 4.1.7 on 2023-02-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administration", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Students",
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
                ("Name", models.TextField(default="", max_length=100)),
                ("Contact", models.IntegerField(default=0)),
                ("Email", models.EmailField(default="", max_length=100)),
                ("Username", models.TextField(default="", max_length=100)),
                ("Password", models.TextField(default="", max_length=100)),
                ("active", models.BooleanField(default=True)),
                ("is_student", models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name="adminuser",
            name="is_admin",
            field=models.BooleanField(default=True),
        ),
    ]
