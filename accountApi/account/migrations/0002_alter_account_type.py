# Generated by Django 3.2.11 on 2022-02-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
