# Generated by Django 3.1.1 on 2020-10-06 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_orderitem_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='name',
        ),
    ]
