# Generated by Django 3.1 on 2020-08-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20200822_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentlyresiding',
            name='bathrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='currentlyresiding',
            name='effected_by_calamities',
            field=models.CharField(default='NO', max_length=3),
        ),
        migrations.AddField(
            model_name='currentlyresiding',
            name='roofing',
            field=models.IntegerField(default=0),
        ),
    ]
