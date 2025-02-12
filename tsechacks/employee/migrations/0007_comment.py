# Generated by Django 2.1.1 on 2019-02-06 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20190206_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=40)),
                ('event_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='employee.Event')),
            ],
        ),
    ]
