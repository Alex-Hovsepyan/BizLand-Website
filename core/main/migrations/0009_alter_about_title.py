# Generated by Django 4.2.7 on 2023-11-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_about_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=80, verbose_name='Title'),
        ),
    ]