# Generated by Django 3.0.3 on 2020-02-05 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('executors', '0001_initial'),
        ('schedules', '0002_auto_20200203_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='supplier_employee',
        ),
        migrations.AddField(
            model_name='schedule',
            name='executor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='executors.Executor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lunchbreak',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lunch_breaks', to='schedules.Schedule'),
        ),
    ]
