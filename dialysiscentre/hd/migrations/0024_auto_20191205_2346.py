# Generated by Django 2.2.7 on 2019-12-06 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hd', '0023_auto_20191205_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='training_details',
            old_name='date',
            new_name='trainingDate',
        ),
        migrations.RenameField(
            model_name='treatments',
            old_name='type',
            new_name='treatmentType',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='runNumber',
        ),
        migrations.AddField(
            model_name='appointments',
            name='appointType',
            field=models.CharField(default=1.0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consultations',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hd.DOCTORS'),
        ),
    ]