# Generated by Django 3.2.5 on 2021-10-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfolio',
            name='project_image',
            field=models.URLField(blank=True, default='https://libum.vercel.app/assets/linktree-features-analytics.webp'),
        ),
    ]
