# Generated by Django 4.1.4 on 2022-12-27 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
