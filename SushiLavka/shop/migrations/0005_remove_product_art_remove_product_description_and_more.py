# Generated by Django 4.2.5 on 2023-10-09 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_delete_filling'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='art',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='types',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='types',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subproducts', to='shop.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
