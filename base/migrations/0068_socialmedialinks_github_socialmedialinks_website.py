# Generated by Django 4.0.1 on 2023-07-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0067_alter_logo_reson_alter_student_role_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedialinks',
            name='github',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socialmedialinks',
            name='website',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
