# Generated by Django 3.2.4 on 2023-02-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninad', '0003_auto_20230219_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='ragadb',
            name='video_link',
            field=models.TextField(default=''),
        ),
    ]
