# Generated by Django 5.1.3 on 2024-12-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypilotapp', '0002_product_features2_product_features3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=200, verbose_name='surrency name thta are avalible for exchnage')),
                ('ex_price', models.IntegerField(default=0, verbose_name='price in usd exchnage')),
                ('limits', models.CharField(blank=True, default='No limits', max_length=300, null=True, verbose_name='exchange limits')),
                ('time_speep', models.CharField(blank=True, max_length=100, null=True, verbose_name='specify how long it will take to exchnage the coins')),
            ],
        ),
        migrations.CreateModel(
            name='spot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000, verbose_name='spots name that will be purchased')),
                ('price', models.IntegerField(default=0, verbose_name='spot priceing')),
            ],
        ),
        migrations.RenameModel(
            old_name='conpany',
            new_name='company',
        ),
    ]
