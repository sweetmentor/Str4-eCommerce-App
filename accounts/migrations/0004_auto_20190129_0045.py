# Generated by Django 2.0.6 on 2019-01-29 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190129_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='unknown', max_length=50),
        ),
    ]