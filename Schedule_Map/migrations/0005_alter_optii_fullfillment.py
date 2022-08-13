# Generated by Django 4.0.6 on 2022-08-10 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule_Map', '0004_alter_optii_fullfillment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optii',
            name='fullfillment',
            field=models.ForeignKey(blank=True, limit_choices_to={'skippable': True}, on_delete=django.db.models.deletion.CASCADE, related_name='crs', to='Schedule_Map.courses'),
        ),
    ]
