# Generated by Django 3.1.4 on 2020-12-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200512_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='meta_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]