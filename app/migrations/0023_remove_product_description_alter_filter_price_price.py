# Generated by Django 4.0.3 on 2022-03-31 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_blog_list_alter_filter_price_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('20000 TO 30000', '20000 TO 30000'), ('30000 TO 40000', '30000 TO 40000'), ('10000 TO 20000', '10000 TO 20000'), ('1000 TO 10000', '1000 TO 10000'), ('40000 TO 50000', '40000 TO 50000')], max_length=68),
        ),
    ]
