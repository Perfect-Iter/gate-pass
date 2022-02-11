# Generated by Django 3.2.9 on 2022-02-11 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('adm_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('Major', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('signed-in', 'signed-in'), ('signed-out', 'signed-out'), ('passive', 'passive')], max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=12)),
                ('type', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.student')),
            ],
        ),
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('adm_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.student')),
                ('serial_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.device')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]