# Generated by Django 4.1.6 on 2023-04-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_alter_journey_entry_time_alter_journey_exit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='entry_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='journey',
            name='exit_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=''),
        ),
    ]
