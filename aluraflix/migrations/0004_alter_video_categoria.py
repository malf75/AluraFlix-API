# Generated by Django 5.0.7 on 2024-07-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluraflix', '0003_categoria_alter_video_url_video_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='categoria',
            field=models.ManyToManyField(blank=True, default=1, null=True, to='aluraflix.categoria'),
        ),
    ]