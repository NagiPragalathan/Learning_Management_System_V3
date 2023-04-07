# Generated by Django 3.0.5 on 2023-04-07 05:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0045_note_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterEditPage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('InstituteName', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('PhoneNumber', models.CharField(max_length=200)),
                ('EXN', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('last_updated_date', models.DateField(default=datetime.datetime(2023, 4, 7, 5, 11, 21, 522627, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='logo',
            fields=[
                ('L_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Reson', models.CharField(max_length=200)),
                ('image', models.ImageField(default='images/user_image.png', upload_to='logo')),
                ('last_updated_date', models.DateField(default=datetime.datetime(2023, 4, 7, 5, 11, 21, 507002, tzinfo=utc))),
            ],
            options={
                'get_latest_by': ['image'],
            },
        ),
        migrations.CreateModel(
            name='SocialMediaLinks',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Twitter', models.CharField(max_length=200)),
                ('Facebook', models.CharField(max_length=200)),
                ('Instagram', models.CharField(max_length=200)),
                ('LinkedIn', models.CharField(max_length=200)),
                ('last_updated_date', models.DateField(default=datetime.datetime(2023, 4, 7, 5, 11, 21, 522627, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('T_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('image', models.ImageField(default='images/user_image.png', upload_to='Testimonials/%Y/%m/%d')),
                ('description', models.CharField(max_length=200)),
                ('categories', models.CharField(max_length=200)),
                ('last_updated_date', models.DateField(default=datetime.datetime(2023, 4, 7, 5, 11, 21, 507002, tzinfo=utc))),
            ],
        ),
    ]