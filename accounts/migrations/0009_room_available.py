# Generated by Django 3.0.8 on 2020-08-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_room_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='available',
            field=models.CharField(default='YES', max_length=3),
            preserve_default=False,
        ),
    ]