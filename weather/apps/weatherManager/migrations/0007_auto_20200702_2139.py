# Generated by Django 3.0.7 on 2020-07-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherManager', '0006_auto_20200702_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Температура'),
        ),
    ]
