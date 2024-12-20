# Generated by Django 4.0.2 on 2024-10-12 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycling', '0009_alter_fundrequest_airtime_choice_and_more'),
    ]

    operations = [
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
