# Generated by Django 3.1.2 on 2020-11-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subcription',
            fields=[
                ('sub_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sub_name', models.CharField(max_length=255, verbose_name='Subcription Name')),
                ('sub_month', models.IntegerField(verbose_name='Month Of Plan')),
                ('sub_price', models.IntegerField(verbose_name='Subcription Price')),
                ('final_price', models.IntegerField(verbose_name='final Price')),
                ('sub_imgcount', models.IntegerField(default=None, null=True, verbose_name='Subcription Provide Theme')),
                ('sub_remain_imgcount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Subcription Remain Theme')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], max_length=10)),
            ],
        ),
    ]
