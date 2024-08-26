

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ticket",
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
                    "ticket_category",
                    models.CharField(
                        choices=[
                            ("general", "عامة"),
                            ("technical", "تقنية"),
                            ("billing", "الدفع"),
                            ("complaint", "شكوى"),
                            ("suggestion", "اقتراح"),
                            ("feature_request", "طلب اضافة ميزة"),
                            ("other", "اخرى"),
                        ],
                        default="general",
                        max_length=255,
                    ),
                ),
                ("ticket_title", models.CharField(max_length=255)),
                ("ticket_description", models.TextField()),
                (
                    "ticket_status",
                    models.CharField(
                        choices=[
                            ("open", "Open"),
                            ("in_progress", "In Progress"),
                            ("closed", "Closed"),
                        ],
                        default="open",
                        max_length=20,
                    ),
                ),
                ("ticket_created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "ticket_creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("comment_text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "comment_creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
                (
                    "ticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="support.ticket",
                    ),
                ),
            ],
        ),
    ]