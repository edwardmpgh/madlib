# Generated by Django 2.2.2 on 2019-06-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='madlibs',
            name='madlib',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
