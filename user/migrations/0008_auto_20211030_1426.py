# Generated by Django 3.1.13 on 2021-10-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_userstatus_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userstatus',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
