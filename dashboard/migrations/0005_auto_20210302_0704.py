# Generated by Django 3.1.6 on 2021-03-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_student_info_expire_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student_info',
            options={'verbose_name': 'student information', 'verbose_name_plural': 'students information'},
        ),
        migrations.AddField(
            model_name='student_info',
            name='next_date',
            field=models.DateField(null=True),
        ),
    ]