# Generated by Django 2.2.7 on 2019-12-06 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hd', '0021_auto_20191205_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outclinics',
            name='machine',
        ),
        migrations.AddField(
            model_name='treatments',
            name='machine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hd.MACHINES'),
        ),
    ]
