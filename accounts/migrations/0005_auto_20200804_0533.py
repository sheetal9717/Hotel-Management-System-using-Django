# Generated by Django 3.0.8 on 2020-08-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200804_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('NAC', 'NON-AC'), ('DEL', 'DELUXE'), ('YAC', 'AC')], max_length=3),
        ),
    ]
