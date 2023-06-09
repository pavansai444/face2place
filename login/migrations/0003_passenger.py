# Generated by Django 4.1.6 on 2023-04-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_journeys_journey'),
    ]

    operations = [
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='pics')),
                ('sex', models.CharField(default='Male', max_length=20)),
                ('status', models.CharField(default='NOT Travelling', max_length=20)),
                ('balance', models.IntegerField(blank=True, default=1, null=True)),
                ('password', models.CharField(default='**', max_length=20)),
            ],
        ),
    ]
