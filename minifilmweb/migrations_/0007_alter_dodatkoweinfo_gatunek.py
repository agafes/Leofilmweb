# Generated by Django 4.0.4 on 2022-04-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minifilmweb', '0006_alter_dodatkoweinfo_gatunek_aktor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Dramat'), (3, 'Sci-fi'), (1, 'Horror'), (0, 'Inne'), (2, 'Komedia')], default=0),
        ),
    ]
