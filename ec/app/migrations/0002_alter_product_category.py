# Generated by Django 4.1.5 on 2023-06-08 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ML', 'Milk'), ('CR', 'Curd'), ('LS', 'Lassi'), ('PN', 'Paneer'), ('MS', 'Milkshake'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IC', 'Icecream'), ('KL', 'Kulfi')], max_length=2),
        ),
    ]
