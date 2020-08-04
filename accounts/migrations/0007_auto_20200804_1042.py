# Generated by Django 3.0.8 on 2020-08-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200804_0536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='beds',
        ),
        migrations.RemoveField(
            model_name='room',
            name='category',
        ),
        migrations.AddField(
            model_name='booking',
            name='person',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]