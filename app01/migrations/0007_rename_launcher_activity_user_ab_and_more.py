# Generated by Django 4.0.6 on 2022-12-14 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_alter_activity_activitybegin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='launcher',
            new_name='user_ab',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='poster',
            new_name='user_ab',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='dishSeller',
            new_name='user_ab',
        ),
    ]