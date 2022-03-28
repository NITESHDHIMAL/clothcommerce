# Generated by Django 4.0.3 on 2022-03-26 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_categories_data_toggle_alter_categories_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter_Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(choices=[('30000 TO 40000', '30000 TO 40000'), ('1000 TO 10000', '1000 TO 10000'), ('10000 TO 20000', '10000 TO 20000'), ('40000 TO 50000', '40000 TO 50000'), ('20000 TO 30000', '20000 TO 30000')], max_length=68)),
            ],
        ),
    ]
