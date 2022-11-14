# Generated by Django 4.1.3 on 2022-11-14 13:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseUuid",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("9a84d85b-c908-454f-9d3f-7f8ec8bff467"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Samples",
            fields=[
                (
                    "baseuuid_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="samples.baseuuid",
                    ),
                ),
                (
                    "sample_name",
                    models.CharField(max_length=100, verbose_name="Название образца"),
                ),
            ],
            bases=("samples.baseuuid",),
        ),
    ]
