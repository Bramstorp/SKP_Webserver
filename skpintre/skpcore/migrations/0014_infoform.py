# Generated by Django 3.0.5 on 2020-06-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skpcore', '0013_auto_20200615_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infoform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, null=True)),
            ],
        ),
    ]
