# Generated by Django 4.0.4 on 2022-05-24 17:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_delete_usercreatesignup_customusermodel_parent_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
