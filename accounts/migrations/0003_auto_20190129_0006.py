# Generated by Django 2.0.6 on 2019-01-29 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190128_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='', max_length=50),
        ),
    ]