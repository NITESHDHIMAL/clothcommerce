# Generated by Django 4.0.3 on 2022-03-26 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_alter_filter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('20000 TO 30000', '20000 TO 30000'), ('30000 TO 40000', '30000 TO 40000'), ('10000 TO 20000', '10000 TO 20000'), ('40000 TO 50000', '40000 TO 50000'), ('1000 TO 10000', '1000 TO 10000')], max_length=68),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]