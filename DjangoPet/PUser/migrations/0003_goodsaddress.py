# Generated by Django 2.1.8 on 2019-11-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PUser', '0002_user_identity'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recver', models.CharField(max_length=64)),
                ('address', models.TextField()),
                ('post_number', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
                ('state', models.IntegerField()),
            ],
        ),
    ]
