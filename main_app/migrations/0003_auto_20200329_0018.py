# Generated by Django 2.2.6 on 2020-03-29 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='feeding datesss'),
        ),
    ]
