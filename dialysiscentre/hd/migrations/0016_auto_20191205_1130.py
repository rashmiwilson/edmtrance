# Generated by Django 2.2.7 on 2019-12-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hd', '0015_auto_20191205_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caretakers',
            options={'verbose_name_plural': 'Caretakers'},
        ),
        migrations.AlterModelOptions(
            name='nurses',
            options={'verbose_name_plural': 'Nurses'},
        ),
        migrations.AlterModelOptions(
            name='training_details',
            options={'verbose_name_plural': 'Training Completed'},
        ),
        migrations.AlterModelOptions(
            name='trainings',
            options={'verbose_name_plural': 'TRAININGS'},
        ),
        migrations.AlterField(
            model_name='nurses',
            name='degree',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='nurses',
            name='seniority',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='training_details',
            name='cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='training_details',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='training_details',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainings',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainings',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
