# Generated by Django 4.1.7 on 2023-04-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_traveler_alter_post_travelers_delete_travelers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveler',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='home/post_images/travelers_avatars'),
        ),
    ]
