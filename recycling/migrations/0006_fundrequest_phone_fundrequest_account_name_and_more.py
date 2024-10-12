# Generated by Django 4.0.2 on 2024-10-11 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycling', '0005_rename_points_trashrequest_earned'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundrequest',
            name='Phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='fundrequest',
            name='account_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='fundrequest',
            name='airtime_choice',
            field=models.CharField(choices=[('MTN Airtime', 'MTN Airtime'), ('GLO Airtime', 'GLO Airtime'), ('AirTel Airtime', 'AirTel Airtime'), ('9Mobile Airtime', '9Mobile Airtime')], default='Airtime Network', max_length=100),
        ),
        migrations.AddField(
            model_name='fundrequest',
            name='bank',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='fundrequest',
            name='data_choice',
            field=models.CharField(choices=[('MTN Data', 'MTN Data'), ('GLO Data', 'GLO Data'), ('AirTel Data', 'AirTel Data'), ('9Mobile Data', '9Mobile Data')], default='Data Network', max_length=100),
        ),
        migrations.AddField(
            model_name='fundrequest',
            name='health_choice',
            field=models.CharField(choices=[('Choose purpose', 'Choose purpose'), ('Medical test', 'Medical test'), ('Hospital bill', 'Hospital bill'), ('others', 'Others')], default='Health Network', max_length=100),
        ),
        migrations.AddField(
            model_name='fundrequest',
            name='school_choice',
            field=models.CharField(choices=[('School fee', 'School fee'), ('Book / Course materials', 'Book / Course materials'), ('others', 'Others')], default='School Purpose', max_length=100),
        ),
        migrations.AlterField(
            model_name='fundrequest',
            name='account_no',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='fundrequest',
            name='withdraw_type',
            field=models.CharField(choices=[('Withdraw purpose', 'Withdraw purpose'), ('Health', 'Health Care Need'), ('School', 'Educational Need'), ('EcoFashion', 'Eco Fashion'), ('Airtime', 'Airtime'), ('Data', 'Data')], default='Withdraw purpose', max_length=100),
        ),
    ]