# Generated by Django 4.0.2 on 2024-06-17 21:21

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recycling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trashrequest',
            name='trash_types',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Nylon', 'Nylon'), ('Bottle', 'Bottle'), ('Plastic', 'Plastic')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='trashrequest',
            name='trash_type',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
