# Generated by Django 2.2.7 on 2019-11-11 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_app', '0003_auto_20191111_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialnetworks_types',
            old_name='title',
            new_name='title_cn',
        ),
    ]
