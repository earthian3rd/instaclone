# Generated by Django 4.0.2 on 2022-03-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]