# Generated by Django 3.2.8 on 2022-06-15 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0003_portfiloproject_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('secondTitle', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.resume')),
            ],
        ),
    ]
