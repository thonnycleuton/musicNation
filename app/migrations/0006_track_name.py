# Generated by Django 2.0.5 on 2018-06-30 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180627_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='name',
            field=models.CharField(default='Breath', max_length=100),
            preserve_default=False,
        ),
    ]