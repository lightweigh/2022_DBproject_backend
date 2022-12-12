# Generated by Django 4.0.6 on 2022-12-11 07:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_remove_user_usernumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishesSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='slide', verbose_name='轮播图片')),
                ('sort', models.IntegerField(default=0, verbose_name='排列顺序')),
                ('create_date', models.DateTimeField(default=django.utils.datetime_safe.datetime.now, verbose_name='添加时间')),
                ('dishes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app01.dish', verbose_name='菜品')),
            ],
        ),
    ]
