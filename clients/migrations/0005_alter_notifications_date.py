# Generated by Django 4.1.7 on 2023-06-13 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0004_alter_notifications_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notifications",
            name="date",
            field=models.DateField(
                default=datetime.date(2023, 6, 13), verbose_name="Fecha"
            ),
        ),
    ]
