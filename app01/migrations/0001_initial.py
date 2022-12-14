# Generated by Django 4.0.6 on 2022-12-14 05:39

import app01.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activityId', models.AutoField(primary_key=True, serialize=False)),
                ('activityName', models.CharField(max_length=30, verbose_name='活动名称')),
                ('activityBrief', models.CharField(max_length=30, verbose_name='活动简介')),
                ('activityContent', models.FileField(upload_to=app01.models.user_directory_path, verbose_name='活动详情')),
                ('activityHeadPhoto', models.ImageField(default='default.jpg', null=True, upload_to=app01.models.user_directory_path, verbose_name='活动头图')),
                ('activityBegin', models.DateTimeField(verbose_name='活动开始时间')),
                ('activityEnd', models.DateTimeField(verbose_name='活动结束时间')),
                ('activityPersonCnt', models.IntegerField(default=0, verbose_name='活动参与人数')),
            ],
            options={
                'db_table': 'backend_activity',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blogId', models.AutoField(primary_key=True, serialize=False)),
                ('blogPrivate', models.BooleanField(choices=[(True, '是'), (False, '否')], null=True, verbose_name='是否公开')),
                ('blogTitle', models.CharField(max_length=45, verbose_name='帖子标题')),
                ('blogContent', models.FileField(upload_to='blogs/contents', verbose_name='帖子内容存储路径')),
                ('blogDeliverTime', models.DateTimeField(verbose_name='帖子发布时间')),
                ('blogFavoriterCnt', models.IntegerField(default=0, null=True, verbose_name='帖子的收藏人数')),
                ('blogLikeCnt', models.IntegerField(default=0, null=True, verbose_name='帖子的喜欢人数')),
                ('blogsActivitys', models.ManyToManyField(to='app01.activity')),
            ],
            options={
                'db_table': 'backend_blog',
            },
        ),
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
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('dishId', models.AutoField(primary_key=True, serialize=False)),
                ('dishName', models.CharField(max_length=30, verbose_name='菜品名')),
                ('dishPrice', models.FloatField(verbose_name='菜品价格')),
                ('dishPicture', models.ImageField(default='default.jpg', max_length=25, null=True, upload_to=app01.models.user_directory_path, verbose_name='菜品头像')),
                ('dishStars', models.FloatField(verbose_name='菜品评分')),
                ('dishRaw', models.CharField(default='暂未提供原料信息', max_length=50, null=True, verbose_name='菜品原料')),
                ('dishTaste', models.CharField(default='暂未提供口味信息', max_length=30, null=True, verbose_name='菜品口味')),
                ('dishBrief', models.TextField(default='暂未提供菜品简介', max_length=300, null=True, verbose_name='菜品简介')),
                ('dishFollowerCnt', models.IntegerField(verbose_name='收藏人数')),
                ('dishAvailable', models.BooleanField(choices=[(True, '是'), (False, '否')], null=True, verbose_name='当日售罄')),
                ('dishSeller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='销售窗口')),
            ],
            options={
                'db_table': 'backend_dish',
            },
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('merchantId', models.AutoField(primary_key=True, serialize=False)),
                ('isMerchant', models.BooleanField(choices=[(True, '是'), (False, '否')], verbose_name='是否是商家')),
                ('merchantName', models.CharField(max_length=30, unique=True, verbose_name='窗口名')),
                ('merchantPassword', models.CharField(max_length=25, verbose_name='窗口登录密码')),
                ('merchantPortrait', models.ImageField(upload_to=app01.models.user_directory_path, verbose_name='窗口头像')),
                ('merchantPhone', models.CharField(max_length=11, unique=True, verbose_name='窗口电话')),
                ('merchantStars', models.FloatField(default='10', verbose_name='商家评分')),
                ('merchantAddr', models.CharField(max_length=50, unique=True, verbose_name='窗口地址')),
                ('merchantOpen', models.TimeField(verbose_name='窗口营业起始时间')),
                ('merchantClose', models.TimeField(verbose_name='窗口营业结束时间')),
                ('merchantHead', models.CharField(max_length=30, verbose_name='窗口所属食堂')),
                ('merchantFollowerCnt', models.IntegerField(null=True, verbose_name='收藏人数')),
                ('merchantActivityId', models.ManyToManyField(to='app01.activity')),
                ('user_ab', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'db_table': 'backend_merchant',
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45, unique=True, verbose_name='用户昵称')),
                ('userSignature', models.CharField(blank=True, default='这个人很懒，什么也没留下~', max_length=45, verbose_name='用户个性签名')),
                ('userSex', models.IntegerField(choices=[(0, '女性'), (1, '男性')], default=1, null=True, verbose_name='用户性别')),
                ('userGrade', models.CharField(blank=True, max_length=25, verbose_name='用户年级')),
                ('userPortrait', models.ImageField(default='default.jpg', max_length=25, null=True, upload_to=app01.models.user_directory_path, verbose_name='用户头像')),
                ('userPrefer', models.CharField(blank=True, default='', max_length=25, verbose_name='用户的口味偏好')),
                ('userActivityId', models.ManyToManyField(to='app01.activity')),
                ('userFavoriteDishId', models.ManyToManyField(to='app01.dish')),
                ('userFavoriteMerchantId', models.ManyToManyField(to='app01.merchant')),
                ('user_ab', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'db_table': 'backend_user',
            },
        ),
        migrations.CreateModel(
            name='DishComment',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('commentContent', models.CharField(max_length=300, verbose_name='评论内容')),
                ('commentDeliverTime', models.DateTimeField(verbose_name='发布时间')),
                ('commentSort', models.IntegerField(choices=[(0, '发布'), (1, '收到')], verbose_name='评论性质')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_comment', to='app01.dish')),
            ],
            options={
                'db_table': 'backend_dish_comment',
            },
        ),
        migrations.CreateModel(
            name='BlogPicture',
            fields=[
                ('blogPictureId', models.AutoField(primary_key=True, serialize=False)),
                ('blogPicture', models.ImageField(default='default.jpg', max_length=25, null=True, upload_to='blogs/imgs', verbose_name='帖子照片')),
                ('blogId', models.ManyToManyField(to='app01.blog')),
            ],
            options={
                'db_table': 'backend_blog_picture',
            },
        ),
        migrations.CreateModel(
            name='BlogLabel',
            fields=[
                ('blogLabelId', models.AutoField(primary_key=True, serialize=False)),
                ('blogLabelContent', models.CharField(max_length=30, unique=True, verbose_name='标签名称')),
                ('blogId', models.ManyToManyField(to='app01.blog')),
            ],
            options={
                'db_table': 'backend_blog_Label',
            },
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('commentContent', models.CharField(max_length=300, verbose_name='评论内容')),
                ('commentDeliverTime', models.DateTimeField(verbose_name='发布时间')),
                ('commentSort', models.IntegerField(choices=[(0, '发布'), (1, '收到')], verbose_name='评论性质')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comment', to='app01.blog')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
            ],
            options={
                'db_table': 'backend_blog_comment',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blogsDishes',
            field=models.ManyToManyField(to='app01.dish'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blogsFavoritedUserIds',
            field=models.ManyToManyField(to='app01.myuser'),
        ),
        migrations.AddField(
            model_name='blog',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者'),
        ),
        migrations.CreateModel(
            name='ActivitySlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='slide', verbose_name='轮播图片')),
                ('sort', models.IntegerField(default=0, verbose_name='排列顺序')),
                ('create_date', models.DateTimeField(default=django.utils.datetime_safe.datetime.now, verbose_name='添加时间')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app01.activity', verbose_name='活动内容')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityComment',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('commentContent', models.CharField(max_length=300, verbose_name='评论内容')),
                ('commentDeliverTime', models.DateTimeField(verbose_name='发布时间')),
                ('commentSort', models.IntegerField(choices=[(0, '发布'), (1, '收到')], verbose_name='评论性质')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_comment', to='app01.activity')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
            ],
            options={
                'db_table': 'backend_activity_comment',
            },
        ),
    ]
