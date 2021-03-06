# Generated by Django 2.2.7 on 2019-12-05 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hd', '0010_auto_20191205_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADMINS',
            fields=[
                ('salary', models.IntegerField(null=True)),
                ('staffID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hd.STAFF')),
                ('createts', models.DateTimeField(auto_now_add=True)),
                ('modifyts', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'administrators',
            },
        ),
        migrations.AlterModelOptions(
            name='appointments',
            options={},
        ),
        migrations.AddField(
            model_name='appointments',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hd.ADMINS'),
        ),
        migrations.AddField(
            model_name='inclinics',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hd.ADMINS'),
        ),
    ]
