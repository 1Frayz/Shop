# Generated by Django 4.2.5 on 2023-10-09 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_types_hello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='types',
            name='slug',
        ),
    ]
