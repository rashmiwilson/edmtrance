# Generated by Django 2.2.7 on 2019-12-05 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hd', '0006_auto_20191205_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technicians',
            options={'verbose_name_plural': 'technicians'},
        ),
        migrations.RenameField(
            model_name='technicians',
            old_name='staff',
            new_name='staffID',
        ),
    ]
