# Generated by Django 4.2.5 on 2023-10-11 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_remove_category_image_category_svg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='types',
            old_name='categories',
            new_name='category',
        ),
    ]
