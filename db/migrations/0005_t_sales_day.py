# Generated by Django 5.0.3 on 2024-04-08 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0004_t_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="T_Sales_Day",
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
                ("sale_date", models.DateField()),
                ("sale_date_fr", models.CharField(max_length=50, null=True)),
                ("media_id", models.CharField(max_length=50, null=True)),
                ("customer_id", models.CharField(max_length=50, null=True)),
                ("customer_nm", models.CharField(max_length=100, null=True)),
                ("mkt_cd", models.CharField(max_length=50, null=True)),
                ("mkt_nm", models.CharField(max_length=100, null=True)),
                (
                    "tot_amt",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                ("reg_gbn", models.CharField(max_length=50, null=True)),
                ("sale_note", models.TextField(blank=True, null=True)),
                ("scrap_param", models.TextField(blank=True, null=True)),
                ("reg_dtm", models.DateTimeField(null=True)),
                ("upd_dtm", models.DateTimeField(null=True)),
                ("reg_uid", models.CharField(max_length=50, null=True)),
                ("reg_name", models.CharField(max_length=100, null=True)),
                ("upd_uid", models.CharField(max_length=50, null=True)),
                ("upd_name", models.CharField(max_length=100, null=True)),
                ("reg_ip", models.CharField(max_length=100, null=True)),
                ("upd_ip", models.CharField(max_length=100, null=True)),
            ],
        ),
    ]