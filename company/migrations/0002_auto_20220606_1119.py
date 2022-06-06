# Generated by Django 3.2.13 on 2022-06-06 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobopening',
            name='batch',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='be_percent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='branch',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='cgpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='dead_kt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='diploma_percent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='gap',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='live_kt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='notice',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='offers',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='package',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='tenth_percent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='twelveth_percent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='valid_till',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
