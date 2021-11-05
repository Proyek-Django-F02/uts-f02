# Generated by Django 3.2.8 on 2021-10-25 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_userstatus_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAccepted', models.BooleanField(default=False)),
                ('message', models.CharField(default="Hi! Let's be friend", max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
        migrations.DeleteModel(
            name='Following',
        ),
        migrations.AddField(
            model_name='invitation',
            name='invitee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pengundang', to='user.profile'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='inviter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diundang', to='user.profile'),
        ),
    ]
