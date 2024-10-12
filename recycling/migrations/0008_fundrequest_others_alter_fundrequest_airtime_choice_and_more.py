# Generated by Django 4.0.2 on 2024-10-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycling', '0007_alter_fundrequest_airtime_choice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundrequest',
            name='others',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='fundrequest',
            name='airtime_choice',
            field=models.CharField(choices=[('Airtime Network', 'Airtime Network'), ('MTN Airtime', 'MTN Airtime'), ('GLO Airtime', 'GLO Airtime'), ('AirTel Airtime', 'AirTel Airtime'), ('9Mobile Airtime', '9Mobile Airtime'), ('others', 'Others')], default='Airtime Network', max_length=100),
        ),
        migrations.AlterField(
            model_name='fundrequest',
            name='data_choice',
            field=models.CharField(choices=[('Data Network', 'Data Network'), ('MTN Data', 'MTN Data'), ('GLO Data', 'GLO Data'), ('AirTel Data', 'AirTel Data'), ('9Mobile Data', '9Mobile Data'), ('others', 'Others')], default='Data Network', max_length=100),
        ),
        migrations.AlterField(
            model_name='fundrequest',
            name='health_choice',
            field=models.CharField(choices=[('Choose purpose', 'Choose purpose'), ('Medication', 'Medication'), ('Medical test', 'Medical test'), ('Hospital bill', 'Hospital bill'), ('others', 'Others')], default='Health Network', max_length=100),
        ),
        migrations.AlterField(
            model_name='fundrequest',
            name='school_choice',
            field=models.CharField(choices=[('School Purpose', 'School Purpose'), ('School fee', 'School fee'), ('feeding', 'feeding'), ('Book / Course materials', 'Book / Course materials'), ('others', 'Others')], default='School Purpose', max_length=100),
        ),
    ]
