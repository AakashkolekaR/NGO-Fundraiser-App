# Generated by Django 2.1.1 on 2019-02-06 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='donationtype',
            field=models.CharField(default='money', max_length=40),
        ),
    ]
