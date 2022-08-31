# Generated by Django 3.2.15 on 2022-08-31 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
