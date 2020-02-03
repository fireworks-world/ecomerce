# Generated by Django 3.0.2 on 2020-02-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='productImages')),
                ('created', models.DateTimeField(verbose_name='auto_now_add=True')),
                ('active', models.BooleanField()),
            ],
        ),
    ]
