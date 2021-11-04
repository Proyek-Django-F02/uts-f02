# Generated by Django 3.1.13 on 2021-10-30 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0008_auto_20211030_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='DM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diundang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dm_diundang', to='user.profile')),
                ('pengundang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dm_pengundang', to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Pesan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isi', models.CharField(max_length=300)),
                ('waktu', models.DateTimeField(auto_now_add=True)),
                ('dm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realchat.dm')),
                ('penerima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pesan_penerima', to='user.profile')),
                ('pengirim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pesan_pengirim', to='user.profile')),
            ],
        ),
    ]