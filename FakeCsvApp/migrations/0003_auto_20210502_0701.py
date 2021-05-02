# Generated by Django 3.2 on 2021-05-02 07:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('FakeCsvApp', '0002_auto_20210501_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='schemas',
            name='DateModified',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 7, 1, 43, 399040, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='DownloadSchemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateModified', models.DateTimeField(default=datetime.datetime(2021, 5, 2, 7, 1, 43, 400417, tzinfo=utc))),
                ('File_name', models.CharField(max_length=100)),
                ('Schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DownloadSchema', to='FakeCsvApp.schemas', verbose_name='schema')),
            ],
            options={
                'verbose_name': 'DownloadSchema',
                'verbose_name_plural': 'DownloadSchemas',
            },
        ),
    ]
