# Generated by Django 3.0.14 on 2022-07-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220725_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_shop',
            field=models.BooleanField(null=True),
        ),
    ]
