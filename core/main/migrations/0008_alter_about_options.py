# Generated by Django 4.2.7 on 2023-11-17 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_about_aboutcontent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
    ]