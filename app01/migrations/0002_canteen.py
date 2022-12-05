# Generated by Django 4.0.6 on 2022-12-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canteen',
            fields=[
                ('canteenId', models.AutoField(primary_key=True, serialize=False)),
                ('canteenName', models.CharField(max_length=30, unique=True, verbose_name='食堂名称')),
                ('canteenAddr', models.CharField(max_length=50, unique=True, verbose_name='食堂地址')),
                ('canteenPhone', models.CharField(max_length=11, unique=True, verbose_name='食堂电话')),
            ],
            options={
                'db_table': 'backend_canteen',
            },
        ),
    ]