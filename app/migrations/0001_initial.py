# Generated by Django 4.0.3 on 2022-03-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('active', 'active'), ('', 'default')], max_length=200)),
                ('image', models.ImageField(upload_to='Product_Image/Slider_Image')),
                ('price_image', models.ImageField(upload_to='Product_Image/Slider_Image')),
            ],
        ),
    ]
