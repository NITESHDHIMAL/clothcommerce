# Generated by Django 4.0.3 on 2022-03-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_rename_addres_order_address_alter_filter_price_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('30000 TO 40000', '30000 TO 40000'), ('20000 TO 30000', '20000 TO 30000'), ('10000 TO 20000', '10000 TO 20000'), ('40000 TO 50000', '40000 TO 50000'), ('1000 TO 10000', '1000 TO 10000')], max_length=68),
        ),
    ]
