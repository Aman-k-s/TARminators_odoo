# Generated by Django 5.1.7 on 2025-07-12 08:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userbase', '0003_alter_userbase_profile_alter_userbase_public'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbase',
            old_name='profile',
            new_name='profileImg',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='name',
        ),
        migrations.AddField(
            model_name='userbase',
            name='user',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
