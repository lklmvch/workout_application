# Generated by Django 4.2.13 on 2024-07-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('intro', models.CharField(max_length=250, verbose_name='Intro')),
                ('text', models.TextField(verbose_name='Article text')),
                ('date', models.DateField(verbose_name='Date')),
            ],
        ),
    ]
