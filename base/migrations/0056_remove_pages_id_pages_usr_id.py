# Generated by Django 4.2.1 on 2023-05-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0055_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pages',
            name='id',
        ),
        migrations.AddField(
            model_name='pages',
            name='usr_id',
            field=models.IntegerField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
