# Generated by Django 4.0.5 on 2022-06-16 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tpc_api', '0009_alter_student_photo_delete_eligiblestudents'),
        ('company', '0002_auto_20220606_1119'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobOpening',
        ),
    ]
