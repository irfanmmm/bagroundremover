# Generated by Django 4.2.7 on 2023-11-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_removebaground_remove_bg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removebaground',
            name='remove_bg',
            field=models.ImageField(blank=True, null=True, upload_to='removed_images/'),
        ),
    ]
