# Generated by Django 4.2.3 on 2023-07-17 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(default='unknown', max_length=200)),
                ('description', models.TextField()),
                ('rating', models.FloatField()),
                ('category', models.CharField(max_length=30)),
                ('image', models.ImageField(default='images/none/noimg.jpg', upload_to='images')),
            ],
        ),
    ]
