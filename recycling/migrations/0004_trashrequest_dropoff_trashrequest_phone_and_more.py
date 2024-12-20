# Generated by Django 4.0.2 on 2024-10-11 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recycling', '0003_alter_trashrequest_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='trashrequest',
            name='DropOff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trashrequest',
            name='Phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='trashrequest',
            name='location',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='trashrequest',
            name='pickup',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trashrequest',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='FundRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdraw_type', models.CharField(choices=[('Withdraw purpose', 'Withdraw purpose'), ('Health', 'Health Care Need'), ('School', 'Educational Need'), ('EcoFashion', 'Eco Fashion'), ('EcoFashion', 'Eco Fashion'), ('MTN Airtime', 'MTN Airtime'), ('GLO Airtime', 'GLO Airtime'), ('AirTel Airtime', 'AirTel Airtime'), ('9Mobile Airtime', '9Mobile Airtime'), ('MTN Data', 'MTN Data'), ('GLO Data', 'GLO Data'), ('AirTel Data', 'AirTel Data'), ('9Mobile Data', '9Mobile Data')], default='Withdraw purpose', max_length=100)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('disbursed', models.BooleanField(default=False)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('account_no', models.CharField(max_length=1000)),
                ('seen', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
