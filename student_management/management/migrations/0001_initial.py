# Generated by Django 4.1.9 on 2024-05-31 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Did', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('Dname', models.CharField(default='CS', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cgpa', models.FloatField()),
                ('marksheet', models.FileField(upload_to='marksheets/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.department')),
            ],
        ),
    ]
