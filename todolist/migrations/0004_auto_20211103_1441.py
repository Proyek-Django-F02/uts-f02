# Generated by Django 3.2.7 on 2021-11-03 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_todolist_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='todolist',
            order_with_respect_to='user',
        ),
    ]
