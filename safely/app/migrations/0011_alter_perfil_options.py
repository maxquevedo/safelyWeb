# Generated by Django 3.2.8 on 2021-11-23 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'default_related_name': 'perfil', 'managed': False},
        ),
    ]
