# Generated by Django 3.1 on 2020-08-12 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200811_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='file',
            field=models.FileField(upload_to='../main/static/movies/'),
        ),
    ]
