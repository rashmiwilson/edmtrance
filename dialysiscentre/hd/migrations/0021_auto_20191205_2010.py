# Generated by Django 2.2.7 on 2019-12-06 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hd', '0020_auto_20191205_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caretakers',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hd.STAFF'),
        ),
    ]
