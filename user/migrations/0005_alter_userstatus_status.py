# Generated by Django 3.2.8 on 2021-10-25 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_userstatus_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='status',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]
