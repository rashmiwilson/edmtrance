# Generated by Django 2.2.7 on 2019-12-06 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hd', '0018_auto_20191205_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inclinics',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hd.DOCTORS'),
        ),
    ]