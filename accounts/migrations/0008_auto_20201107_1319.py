# Generated by Django 3.1.2 on 2020-11-07 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor'), ('Clothing', 'Clothing')], max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
