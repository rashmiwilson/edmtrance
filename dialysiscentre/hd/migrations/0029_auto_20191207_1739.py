# Generated by Django 2.2.7 on 2019-12-08 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hd', '0028_auto_20191207_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='treatments',
            name='duration',
        ),
        migrations.AddField(
            model_name='treatments',
            name='treatmentDuration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='treatments',
            name='venousPressure',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, max_length=100, null=True),
        ),
    ]
