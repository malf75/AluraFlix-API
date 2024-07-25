# Generated by Django 5.0.7 on 2024-07-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluraflix', '0002_rename_videos_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(),
        ),
        migrations.AddField(
            model_name='video',
            name='categoria',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='aluraflix.categoria'),
        ),
    ]
