# Generated by Django 5.1.1 on 2024-10-01 12:33

import fruits_web.apps.platforms.models_container.user
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(blank=True, max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('full_name', models.CharField(max_length=128, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('role', models.CharField(default='USER', max_length=30)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', fruits_web.apps.platforms.models_container.user.CustomUserManager()),
            ],
        ),
    ]
