# Generated by Django 5.0.2 on 2024-05-08 13:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Full', 'Full'), ('Completed', 'Completed'), ('Discontinued', 'Discontinued')], default='Open', max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'commission',
                'verbose_name_plural': 'commissions',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('manpower_required', models.PositiveIntegerField()),
                ('open_manpower', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Full', 'Full')], default='Open', max_length=255)),
                ('commission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='commissions.commission')),
            ],
            options={
                'verbose_name': 'job',
                'verbose_name_plural': 'jobs',
                'ordering': ['-status', '-manpower_required', 'role'],
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=255)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applicant', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='commissions.job')),
            ],
            options={
                'verbose_name': 'application',
                'verbose_name_plural': 'applications',
                'ordering': ['-applied_on'],
            },
        ),
    ]
