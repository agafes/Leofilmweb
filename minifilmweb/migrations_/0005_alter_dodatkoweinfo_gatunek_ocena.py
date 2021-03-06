# Generated by Django 4.0.4 on 2022-04-12 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minifilmweb', '0004_dodatkoweinfo_film_dodatkowe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (0, 'Inne'), (2, 'Komedia'), (4, 'Dramat'), (3, 'Sci-fi')], default=0),
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recenzja', models.TextField(blank=True, default='')),
                ('gwiazdki', models.PositiveSmallIntegerField(default=5)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minifilmweb.film')),
            ],
        ),
    ]
