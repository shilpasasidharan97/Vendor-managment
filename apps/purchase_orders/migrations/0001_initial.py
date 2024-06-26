# Generated by Django 5.0.4 on 2024-05-08 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("vendor", "0002_historicalperformance"),
    ]

    operations = [
        migrations.CreateModel(
            name="PurchaseOrder",
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
                ("po_number", models.CharField(max_length=50, unique=True)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                ("delivery_date", models.DateTimeField()),
                ("items", models.JSONField()),
                ("quantity", models.IntegerField()),
                ("status", models.CharField(max_length=20)),
                ("quality_rating", models.FloatField(blank=True, null=True)),
                ("issue_date", models.DateTimeField(auto_now_add=True)),
                ("acknowledgment_date", models.DateTimeField(blank=True, null=True)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchase_orders",
                        to="vendor.vendor",
                    ),
                ),
            ],
        ),
    ]
