# Generated by Django 3.2.13 on 2022-06-07 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpc_api', '0005_auto_20220607_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherinfo',
            name='pos_of_res_four',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='pos_of_res_one',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='pos_of_res_three',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='otherinfo',
            name='pos_of_res_two',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='placementdetails',
            name='placed_org_one',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='placementdetails',
            name='placed_org_three',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='placementdetails',
            name='placed_org_two',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
