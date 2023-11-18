# Generated by Django 4.2.7 on 2023-11-18 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('position', models.CharField(max_length=40, verbose_name='Position')),
                ('social1', models.URLField(verbose_name='Social 1 Url')),
                ('social2', models.URLField(verbose_name='Social 2 Url')),
                ('social3', models.URLField(verbose_name='Social 3 Url')),
                ('social4', models.URLField(verbose_name='Social 4 Url')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
            },
        ),
    ]
