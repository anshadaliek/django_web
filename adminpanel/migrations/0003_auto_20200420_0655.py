# Generated by Django 3.0.5 on 2020-04-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_auto_20200420_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Updated_date',
            field=models.DateTimeField(blank=True, default='2020-04-20 06:55:11'),
        ),
        migrations.AlterField(
            model_name='category',
            name='added_date',
            field=models.DateTimeField(blank=True, default='2020-04-20 06:55:11'),
        ),
    ]
