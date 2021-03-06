# Generated by Django 3.1.6 on 2021-02-24 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_auto_20210224_0622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainer_availability',
            options={'verbose_name': 'trainers availability', 'verbose_name_plural': 'trainers'},
        ),
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
                ('amount', models.FloatField(default=0)),
                ('time', models.TimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.trainer_availability')),
            ],
            options={
                'verbose_name': 'student information',
                'verbose_name_plural': 'studends information',
            },
        ),
    ]
