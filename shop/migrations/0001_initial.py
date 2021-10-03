# Generated by Django 3.2.7 on 2021-10-01 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('currency', models.CharField(choices=[('USD', 'Dollar'), ('UAH', 'Grivna'), ('RUB', 'Rubles'), ('EUR', 'Euro')], default='UAH', max_length=255)),
                ('photo', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('Sport', 'Sport'), ('Hike', 'Hike'), ('For_Children', 'For children'), ('Cars', 'Cars')], default='Sport', max_length=255)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.brand')),
            ],
        ),
    ]