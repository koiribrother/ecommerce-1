# Generated by Django 4.1.3 on 2022-11-24 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_productreview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreview',
            old_name='slug',
            new_name='slugs',
        ),
    ]
