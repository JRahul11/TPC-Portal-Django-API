# Generated by Django 3.2.13 on 2022-06-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpc_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placementdetails',
            name='offer_letter_one',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='placementdetails',
            name='offer_letter_three',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='placementdetails',
            name='offer_letter_two',
            field=models.TextField(blank=True, null=True),
        ),
    ]