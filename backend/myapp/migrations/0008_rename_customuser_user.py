# Generated by Django 4.2.2 on 2024-02-02 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('myapp', '0007_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='User',
        ),
    ]