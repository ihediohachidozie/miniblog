# Generated by Django 5.0.6 on 2024-07-14 00:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-comment_date"]},
        ),
    ]
