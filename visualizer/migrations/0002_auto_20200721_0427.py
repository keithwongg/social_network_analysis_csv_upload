# Generated by Django 3.0.7 on 2020-07-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='Advocate_Name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='referral',
            name='Friend_Name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
