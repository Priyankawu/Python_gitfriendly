# Generated by Django 3.1.5 on 2021-02-01 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, default='', max_length=60)),
                ('lastname', models.CharField(blank=True, default='', max_length=60)),
                ('email', models.CharField(blank=True, default='', max_length=30)),
                ('username', models.CharField(blank=True, default='', max_length=60)),
            ],
        ),
    ]
