# Generated by Django 4.1.4 on 2023-02-02 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_merge_20230128_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='first_confirmation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='second_confirmation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='visibile',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='visibile',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 9, 14, 36, 21, 790414, tzinfo=datetime.timezone.utc)),
        ),
    ]
