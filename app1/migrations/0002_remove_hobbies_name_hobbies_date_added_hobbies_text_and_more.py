# Generated by Django 5.0.6 on 2024-05-25 04:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobbies',
            name='name',
        ),
        migrations.AddField(
            model_name='hobbies',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hobbies',
            name='text',
            field=models.CharField(default='Default Text', max_length=200),
        ),
        migrations.CreateModel(
            name='HobbyDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('hobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.hobbies')),
            ],
        ),
    ]
