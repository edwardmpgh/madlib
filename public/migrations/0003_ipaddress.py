# Generated by Django 2.2.2 on 2019-06-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20190612_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
    ]
