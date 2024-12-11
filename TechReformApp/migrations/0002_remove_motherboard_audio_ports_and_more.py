# Generated by Django 5.1.3 on 2024-11-29 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechReformApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motherboard',
            name='audio_ports',
        ),
        migrations.RemoveField(
            model_name='motherboard',
            name='bluetooth',
        ),
        migrations.RemoveField(
            model_name='motherboard',
            name='ethernet_ports',
        ),
        migrations.RemoveField(
            model_name='motherboard',
            name='video_ports',
        ),
        migrations.RemoveField(
            model_name='motherboard',
            name='wifi',
        ),
        migrations.AddField(
            model_name='motherboard',
            name='wifi_bluetooth',
            field=models.BooleanField(blank=True, help_text='Wi-Fi and Bluetooth support', null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='chipset',
            field=models.CharField(blank=True, choices=[('H510', 'H510'), ('B460', 'B460'), ('H610', 'H610'), ('B660', 'B660'), ('B760', 'B760'), ('Z790', 'Z790'), ('Z890', 'Z890'), ('A520', 'A520'), ('B450', 'B450'), ('B550', 'B550'), ('X570', 'X570'), ('A620', 'A620'), ('B650', 'B650'), ('X670', 'X670'), ('X670E', 'X670E'), ('X870', 'X870'), ('X870E', 'X870E'), ('TRX40', 'TRX40')], help_text='Chipset', max_length=50, null=True),
        ),
    ]