# Generated by Django 5.1.1 on 2024-10-02 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='idUser',
            new_name='id_user',
        ),
    ]
