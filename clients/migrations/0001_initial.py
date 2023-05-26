# Generated by Django 4.1.7 on 2023-05-22 22:51

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Login", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Providers",
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
                (
                    "name",
                    models.CharField(default="", max_length=30, verbose_name="Nombre"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Apellidos"),
                ),
                (
                    "telephone",
                    models.CharField(
                        default="", max_length=12, verbose_name="Teléfono"
                    ),
                ),
                (
                    "logo",
                    models.CharField(default="", max_length=100, verbose_name="Logo"),
                ),
                (
                    "enterprise_name",
                    models.CharField(
                        default="", max_length=100, verbose_name="Nombre de la empresa"
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(max_length=200, verbose_name="Descripción"),
                ),
                (
                    "is_suscribed",
                    models.BooleanField(default=False, verbose_name="Está sustrito"),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Login.perfil",
                        verbose_name="Id de usuario",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Catálogo",
            },
        ),
        migrations.CreateModel(
            name="notifications",
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
                (
                    "title",
                    models.CharField(default="", max_length=15, verbose_name="Titulo"),
                ),
                (
                    "description",
                    models.CharField(
                        default="", max_length=40, verbose_name="Descripción"
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        default=datetime.date(2023, 5, 22), verbose_name="Fecha"
                    ),
                ),
                ("seen", models.BooleanField(default=False, verbose_name="Visto")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notifications",
                        to="Login.perfil",
                        verbose_name="Usuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="directions",
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
                (
                    "estate",
                    models.CharField(default="", max_length=20, verbose_name="Estado"),
                ),
                (
                    "city",
                    models.CharField(default="", max_length=30, verbose_name="Ciudad"),
                ),
                (
                    "cologne",
                    models.CharField(default="", max_length=30, verbose_name="Colonia"),
                ),
                (
                    "street",
                    models.CharField(default="", max_length=30, verbose_name="Calle"),
                ),
                (
                    "outdoor_number",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Número exterior",
                    ),
                ),
                (
                    "indoor_number",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Número interior",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Login.perfil",
                        verbose_name="id de usuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ConvenienceStore",
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
                ("name", models.CharField(max_length=30, verbose_name="Nombre")),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Apellidos"),
                ),
                ("telephone", models.CharField(max_length=12, verbose_name="Teléfono")),
                (
                    "descripcion",
                    models.CharField(max_length=200, verbose_name="Descripción"),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Login.perfil",
                        verbose_name="Id de usuario",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "ConvenienceStores",
            },
        ),
    ]