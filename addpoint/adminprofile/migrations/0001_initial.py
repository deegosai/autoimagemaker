# Generated by Django 3.1.2 on 2020-11-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminprofile',
            fields=[
                ('aid', models.BigAutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='adminpro/', verbose_name='Admin Image')),
                ('fname', models.CharField(max_length=255, verbose_name='Admin First Name')),
                ('lname', models.CharField(max_length=255, verbose_name='Admin Last Name')),
                ('oc', models.TextField(verbose_name='Admin Organization Or Company Name')),
                ('mobile', models.CharField(max_length=12, unique=True, verbose_name='Admin Mobile')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Admin Email')),
                ('password', models.CharField(max_length=255, verbose_name='Admin Password')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], max_length=10)),
            ],
        ),
    ]