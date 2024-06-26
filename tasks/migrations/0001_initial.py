# Generated by Django 5.0.6 on 2024-05-20 19:13

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
                ('todo', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('do_date', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(editable=False, auto_now=True)),
                ('modified', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_task', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
