# Generated by Django 4.2.5 on 2023-10-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0003_coupon_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='description',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]