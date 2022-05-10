# Generated by Django 3.2 on 2022-04-30 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0009_alter_notification_sources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Bookmark'), (2, 'Clap'), (3, 'Comment'), (4, 'Follow'), (5, 'Following Project'), (6, 'Project Violation')]),
        ),
    ]