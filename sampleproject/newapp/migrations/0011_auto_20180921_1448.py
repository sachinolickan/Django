# Generated by Django 2.1.1 on 2018-09-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0010_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/sample_pic')),
                ('resume', models.FileField(upload_to='media/files')),
                ('adress', models.CharField(max_length=50)),
                ('mobno', models.IntegerField(default=10)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
