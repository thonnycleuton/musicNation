# Generated by Django 2.0.5 on 2018-06-27 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='since',
            field=models.DateField(),
        ),
    ]