# Generated by Django 3.1.4 on 2021-01-18 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='system_weight',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='user_weight',
        ),
        migrations.AddField(
            model_name='allocation',
            name='quantity_offline',
            field=models.FloatField(default=1e-05),
        ),
        migrations.AddField(
            model_name='allocation',
            name='system_votes',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='allocation',
            name='user_votes',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allocations', to='portfolio.portfolio'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
