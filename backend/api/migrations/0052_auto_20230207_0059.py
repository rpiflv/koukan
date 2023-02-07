# Generated by Django 3.2.17 on 2023-02-06 15:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_alter_post_expiration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcategories',
            old_name='categories_id',
            new_name='catagories_categories_id',
        ),
        migrations.RenameField(
            model_name='postcategories',
            old_name='post_id',
            new_name='catagories_post_id',
        ),
        migrations.AlterField(
            model_name='post',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 13, 15, 59, 18, 433750, tzinfo=utc)),
        ),
    ]