# Generated by Django 3.1.6 on 2021-03-05 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_trainer_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=23)),
                ('subject', models.CharField(max_length=38)),
                ('message', models.TextField(max_length=900)),
            ],
        ),
    ]
