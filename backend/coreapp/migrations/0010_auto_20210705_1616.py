# Generated by Django 3.2.4 on 2021-07-05 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0009_compilerconfiguration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scratch',
            old_name='c_code',
            new_name='source_code',
        ),
        migrations.RenameField(
            model_name='scratch',
            old_name='assembly',
            new_name='target_asm',
        ),
    ]
