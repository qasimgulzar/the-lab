# Generated by Django 3.2.6 on 2021-08-25 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminportal', '0003_auto_20210824_0939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='intructor_designation',
            new_name='instructor_designation',
        ),
    ]
