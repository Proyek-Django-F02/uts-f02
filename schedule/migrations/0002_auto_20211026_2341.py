# Generated by Django 3.2.8 on 2021-10-26 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='date',
        ),
        migrations.AddField(
            model_name='activity',
            name='day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='activity',
            name='month',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='activity',
            name='year',
            field=models.IntegerField(default=2021),
        ),
    ]