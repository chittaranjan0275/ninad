# Generated by Django 3.2.12 on 2023-01-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RagaDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=255)),
                ('thaat', models.CharField(max_length=255)),
                ('vadi', models.CharField(max_length=255)),
                ('samvadi', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('aaroh', models.CharField(max_length=255)),
                ('aavaroh', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('link_slug', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
