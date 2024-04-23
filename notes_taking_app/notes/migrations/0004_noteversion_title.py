# Generated by Django 5.0.2 on 2024-02-20 17:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_note_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteversion',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
