# Generated by Django 3.0.8 on 2020-07-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0008_auto_20200702_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='salt_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]