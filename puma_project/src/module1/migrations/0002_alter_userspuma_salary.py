# Generated by Django 4.2.4 on 2023-08-29 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userspuma',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
