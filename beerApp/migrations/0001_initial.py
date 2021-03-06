# Generated by Django 2.0.4 on 2018-04-30 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField()),
                ('brewery', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('subtype', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
    ]
