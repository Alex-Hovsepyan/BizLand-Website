# Generated by Django 4.2.7 on 2023-11-18 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categories')),
            ],
        ),
    ]