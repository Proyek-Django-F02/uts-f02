# Generated by Django 3.2.8 on 2021-10-30 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20211025_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_status', to='user.profile'),
        ),
    ]
