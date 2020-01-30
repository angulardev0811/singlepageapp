# Generated by Django 3.0.2 on 2020-01-27 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0004_auto_20200127_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_names', models.CharField(max_length=30)),
                ('locations', models.CharField(max_length=30)),
                ('quotes', models.CharField(max_length=250)),
                ('images', models.ImageField(default='../static/img/customer/customer-1.png', upload_to='customer/')),
            ],
        ),
    ]