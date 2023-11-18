# Generated by Django 4.2.7 on 2023-11-18 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=60, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('date_time', models.DateTimeField(auto_now=True, verbose_name='Date & Time')),
            ],
        ),
    ]