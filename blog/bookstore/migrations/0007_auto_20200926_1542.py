# Generated by Django 3.1.1 on 2020-09-26 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_customer_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, default='preson.png', null=True, upload_to=''),
        ),
    ]
