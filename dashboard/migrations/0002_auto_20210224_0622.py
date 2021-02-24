# Generated by Django 3.1.6 on 2021-02-24 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curriculums',
            options={'verbose_name': 'django course curriculums', 'verbose_name_plural': 'curriculum'},
        ),
        migrations.CreateModel(
            name='trainer_availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.TimeField()),
                ('students_number', models.IntegerField(default=0, null=True)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
