"""
Custom migration that populate NotificationType table with default values.
"""

from typing import Any

from core.models import NotificationType
from django.db import migrations

DEFAULT_VALUES = ("admin", "like", "repost", "reply")


def populate_table(apps: Any, schema_editor: Any) -> None:
    """Populates table with default values."""
    for value in DEFAULT_VALUES:
        NotificationType.objects.create(name=value)


def reverse_table_population(apps: Any, schema_editor: Any) -> None:
    """Reverse table population."""
    for value in DEFAULT_VALUES:
        NotificationType.objects.get(name=value).delete()


class Migration(migrations.Migration):
    """Creates django migration that writes data to the database."""

    dependencies = [
        ("core", "0002_populate_country_table"),
    ]

    operations = [
        migrations.RunPython(
            code=populate_table,
            reverse_code=reverse_table_population,
        )
    ]
