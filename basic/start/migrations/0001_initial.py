# Generated by Django 5.1.4 on 2024-12-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('ram_size', models.PositiveIntegerField()),
                ('storage_capacity', models.PositiveIntegerField()),
                ('screen_size', models.DecimalField(decimal_places=1, max_digits=4)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('manufacture_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.PositiveIntegerField()),
            ],
        ),
    ]
