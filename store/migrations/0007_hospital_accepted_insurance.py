# Generated by Django 3.1.1 on 2023-06-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20230619_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='accepted_insurance',
            field=models.CharField(default='NHIF accredited', max_length=5000),
        ),
    ]
