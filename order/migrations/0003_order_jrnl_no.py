# Generated by Django 4.0.6 on 2022-07-15 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_account_number_alter_order_screenshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='jrnl_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]