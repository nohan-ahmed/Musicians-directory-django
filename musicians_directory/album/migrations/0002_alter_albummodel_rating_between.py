# Generated by Django 5.0.3 on 2024-05-04 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='Rating_between',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=1),
        ),
    ]
