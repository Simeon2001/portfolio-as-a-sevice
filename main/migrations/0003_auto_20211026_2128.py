# Generated by Django 3.2.5 on 2021-10-26 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211026_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainfolio',
            name='welcome_image',
            field=models.URLField(blank=True, default='https://libum.vercel.app/assets/linktree-features-analytics.webp'),
        ),
        migrations.AlterField(
            model_name='mainfolio',
            name='welcome_text',
            field=models.CharField(default='welcome to my portfolio page', max_length=150),
        ),
    ]
