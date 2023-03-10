# Generated by Django 3.2.4 on 2023-02-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninad', '0002_auto_20230122_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ragadb',
            name='naam',
        ),
        migrations.AddField(
            model_name='ragadb',
            name='aaroh_hindi',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ragadb',
            name='aavaroh_hindi',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ragadb',
            name='info_hindi',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ragadb',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ragadb',
            name='name_hindi',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ragadb',
            name='samvadi_hindi',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ragadb',
            name='thaat_hindi',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ragadb',
            name='time_hindi',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ragadb',
            name='vadi_hindi',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ragadb',
            name='aaroh',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ragadb',
            name='aavaroh',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ragadb',
            name='info',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ragadb',
            name='link_slug',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ragadb',
            name='samvadi',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ragadb',
            name='thaat',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ragadb',
            name='time',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ragadb',
            name='vadi',
            field=models.TextField(default=''),
        ),
    ]
