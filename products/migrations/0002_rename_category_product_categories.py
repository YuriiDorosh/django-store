# Generated by Django 3.2.13 on 2023-07-30 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categories',
        ),
    ]
