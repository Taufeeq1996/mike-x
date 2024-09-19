# Generated by Django 5.0.7 on 2024-07-29 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Anonymous', max_length=15, null='false', verbose_name='Name')),
                ('body', models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created DateTime')),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
