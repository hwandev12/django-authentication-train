# Generated by Django 4.0.4 on 2022-05-24 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_usercreatesignup_remove_customusermodel_parent_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserCreateSignup',
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='parent_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
