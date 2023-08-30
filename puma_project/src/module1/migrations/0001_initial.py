# Generated by Django 4.2.4 on 2023-08-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersPuma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.TextField()),
                ('office', models.TextField()),
                ('age', models.IntegerField()),
                ('start_date', models.DateField(null=True)),
                ('salary', models.DecimalField(decimal_places=50, max_digits=100)),
            ],
        ),
    ]
