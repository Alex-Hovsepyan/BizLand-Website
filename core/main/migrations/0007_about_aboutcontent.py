# Generated by Django 4.2.7 on 2023-11-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('text1', models.TextField(verbose_name='Text 1')),
                ('text2', models.TextField(verbose_name='Text 2')),
            ],
        ),
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=40, verbose_name='Icon')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'About Content',
                'verbose_name_plural': 'About Content',
            },
        ),
    ]
