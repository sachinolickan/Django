# Generated by Django 2.1.1 on 2018-09-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_delete_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
