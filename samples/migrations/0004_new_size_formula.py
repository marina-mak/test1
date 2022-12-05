# Generated by Django 4.1.3 on 2022-12-05 13:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("samples", "0003_add_formula"),
    ]

    operations = [
        migrations.AlterField(
            model_name="baseuuid",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("ef51d3ef-662c-4b20-8129-ece7463d95e2"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="samples",
            name="formula",
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
