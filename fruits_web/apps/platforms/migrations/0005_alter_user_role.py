# Generated by Django 5.1.1 on 2024-10-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0004_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='user', max_length=30),
        ),
    ]
