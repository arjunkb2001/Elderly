# Generated by Django 4.2.3 on 2024-03-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_homenurse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=200)),
                ('contact', models.CharField(max_length=20)),
                ('direction_instructions', models.TextField(max_length=200)),
            ],
        ),
    ]