# Generated by Django 4.0 on 2022-01-19 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('address_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('address2', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(max_length=20)),
                ('city_id', models.IntegerField()),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Address',
            },
        ),
    ]
