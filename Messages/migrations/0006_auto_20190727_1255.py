# Generated by Django 2.0.5 on 2019-07-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages', '0005_auto_20190727_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='messages', to='Messages.Tag'),
        ),
    ]
