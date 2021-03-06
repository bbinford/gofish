# Generated by Django 2.1.7 on 2019-04-06 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('each_additional_person', models.IntegerField()),
                ('min_capacity', models.IntegerField()),
                ('description', models.TextField(max_length=350)),
                ('start_time', models.TimeField()),
                ('duration', models.DurationField()),
                ('type', models.CharField(choices=[('pr', 'Private Trip'), ('sr', 'Shared Trip')], default='pr', max_length=2)),
            ],
        ),
    ]
