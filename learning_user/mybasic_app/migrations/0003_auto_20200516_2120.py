# Generated by Django 2.2.5 on 2020-05-16 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybasic_app', '0002_auto_20200516_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pict',
            field=models.ImageField(blank=True, default='photo_defaut_profile', upload_to='profile_piccs'),
        ),
    ]
