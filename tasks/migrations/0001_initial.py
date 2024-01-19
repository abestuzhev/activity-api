# Generated by Django 5.0.1 on 2024-01-10 14:26

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
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('text', models.CharField(max_length=2000, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
