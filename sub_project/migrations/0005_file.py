# Generated by Django 2.0.5 on 2018-08-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_project', '0004_auto_20180807_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepath', models.FileField(upload_to='files/', verbose_name='')),
            ],
        ),
    ]
