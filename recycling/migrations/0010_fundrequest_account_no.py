# Generated by Django 4.0.2 on 2024-10-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycling', '0009_alter_trashrequest_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundrequest',
            name='account_no',
            field=models.CharField(default='my accunt no', max_length=1000),
            preserve_default=False,
        ),
    ]
