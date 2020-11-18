# Generated by Django 3.1.2 on 2020-11-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homepost',
            fields=[
                ('hp_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hp_img', models.ImageField(upload_to='homepost/', verbose_name='Home Post Image')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], max_length=10)),
            ],
        ),
    ]
