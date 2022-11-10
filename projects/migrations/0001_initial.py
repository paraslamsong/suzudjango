# Generated by Django 4.0.5 on 2022-11-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('info', models.CharField(default='', max_length=120)),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.CharField(max_length=120, null=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
