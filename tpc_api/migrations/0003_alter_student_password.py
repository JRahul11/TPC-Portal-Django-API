# Generated by Django 3.2.12 on 2022-04-30 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpc_api', '0002_auto_20220416_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default='dypatil@123', max_length=100),
        ),
    ]