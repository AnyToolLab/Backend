# Generated by Django 5.1.2 on 2024-11-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='qrcode/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
