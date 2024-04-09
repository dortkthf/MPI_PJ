# Generated by Django 5.0.3 on 2024-04-08 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("db", "0002_delete_t_depts_delete_t_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="T_DEPTS",
            fields=[
                (
                    "dept_code",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("dept_name", models.CharField(max_length=50)),
                ("sort_code", models.IntegerField(null=True)),
                ("dept_note", models.CharField(blank=True, max_length=255, null=True)),
                ("reg_dtm", models.DateTimeField()),
                ("upd_dtm", models.DateTimeField(blank=True, null=True)),
                ("del_dtm", models.DateTimeField(blank=True, null=True)),
                ("reg_uid", models.CharField(max_length=50)),
                ("upd_uid", models.CharField(blank=True, max_length=50, null=True)),
                ("del_uid", models.CharField(blank=True, max_length=50, null=True)),
                ("reg_name", models.CharField(max_length=50)),
                ("upd_name", models.CharField(blank=True, max_length=50, null=True)),
                ("del_name", models.CharField(blank=True, max_length=50, null=True)),
                ("reg_ip", models.CharField(blank=True, max_length=50, null=True)),
                ("upd_ip", models.CharField(blank=True, max_length=50, null=True)),
                ("del_ip", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]