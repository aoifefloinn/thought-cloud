# Generated by Django 3.1.7 on 2021-04-07 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(default='', max_length=10, unique=True, verbose_name='nickname'),
        ),
    ]
