# Generated by Django 4.2.7 on 2023-11-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_featuredservices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredservices',
            name='icon',
            field=models.CharField(max_length=40, verbose_name='Icon'),
        ),
    ]
