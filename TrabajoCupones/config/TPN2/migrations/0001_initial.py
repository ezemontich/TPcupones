# Generated by Django 4.1.3 on 2022-11-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descuentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('discount', models.CharField(choices=[('4', '4%'), ('12', '12%'), ('16', '16%'), ('28', '28%')], max_length=3)),
                ('available', models.BooleanField()),
            ],
        ),
    ]
