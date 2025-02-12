# Generated by Django 2.1.1 on 2019-02-06 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evname', models.CharField(max_length=40)),
                ('evloc', models.CharField(max_length=40)),
                ('evdate', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('evaddr', models.CharField(max_length=200)),
                ('evdesc', models.CharField(max_length=200)),
                ('evduration', models.CharField(max_length=40)),
                ('evexpectedfund', models.CharField(max_length=40)),
                ('evpic_path', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
