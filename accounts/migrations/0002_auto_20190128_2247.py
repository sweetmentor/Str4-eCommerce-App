# Generated by Django 2.0.6 on 2019-01-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='unknown', max_length=50),
        ),
    ]