# Generated by Django 3.1.2 on 2020-11-07 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_product_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tags',
            new_name='tag',
        ),
    ]
