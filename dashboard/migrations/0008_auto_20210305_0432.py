# Generated by Django 3.1.6 on 2021-03-05 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_contact_messages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact_messages',
            options={'verbose_name': 'contact message', 'verbose_name_plural': 'contact messages'},
        ),
    ]
