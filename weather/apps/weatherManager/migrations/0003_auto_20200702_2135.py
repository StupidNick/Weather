# Generated by Django 3.0.7 on 2020-07-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherManager', '0002_auto_20200702_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Температура'),
        ),
    ]