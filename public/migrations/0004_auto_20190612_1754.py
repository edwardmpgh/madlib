# Generated by Django 2.2.2 on 2019-06-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_ipaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddress',
            name='ip',
            field=models.GenericIPAddressField(unique=True),
        ),
    ]
