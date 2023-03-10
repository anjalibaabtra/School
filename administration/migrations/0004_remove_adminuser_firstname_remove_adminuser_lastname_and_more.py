# Generated by Django 4.1.7 on 2023-02-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administration", "0003_alter_students_contact"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="adminuser",
            name="Firstname",
        ),
        migrations.RemoveField(
            model_name="adminuser",
            name="Lastname",
        ),
        migrations.RemoveField(
            model_name="adminuser",
            name="Name",
        ),
        migrations.RemoveField(
            model_name="students",
            name="is_student",
        ),
        migrations.AddField(
            model_name="adminuser",
            name="is_student",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="adminuser",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="students",
            name="active",
            field=models.BooleanField(default=False),
        ),
    ]
