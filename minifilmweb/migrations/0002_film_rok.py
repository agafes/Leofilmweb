# Generated by Django 4.0.4 on 2022-04-11 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minifilmweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='rok',
            field=models.PositiveSmallIntegerField(default=2000),
        ),
    ]
